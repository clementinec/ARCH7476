import warnings
from typing import Iterable, Optional, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

try:
    from sklearn.model_selection import learning_curve, validation_curve
except Exception:  # pragma: no cover - optional at authoring time
    learning_curve = None
    validation_curve = None


def set_style():
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update({
        "figure.figsize": (8, 5),
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "legend.fontsize": 10,
        "figure.dpi": 120,
    })


def plot_cv_folds(n_samples: int, cv_splits: Iterable[Tuple[np.ndarray, np.ndarray]], title: str = "Cross-validation folds"):
    """Visualize train/test membership across CV splits.

    Parameters
    ----------
    n_samples: total number of samples
    cv_splits: iterable of (train_idx, test_idx)
    title: plot title
    """
    set_style()
    # Materialize splits once for reuse
    splits = list(cv_splits)
    fold_matrix = np.zeros((len(splits), n_samples), dtype=int)
    for i, (train_idx, test_idx) in enumerate(splits):
        fold_matrix[i, train_idx] = 1  # train
        fold_matrix[i, test_idx] = 2  # test
    cmap = ListedColormap(["#e0e0e0", "#4CAF50", "#F44336"])
    plt.imshow(fold_matrix, aspect="auto", interpolation="nearest", cmap=cmap, vmin=0, vmax=2)
    plt.yticks(range(len(splits)), [f"Fold {i+1}" for i in range(len(splits))])
    plt.xticks([])
    plt.xlabel("Sample index")
    plt.title(title)
    plt.tight_layout()
    return plt.gca()


def plot_error_bars(
    df: pd.DataFrame,
    group_col: str,
    value_col: str,
    ci: float = 0.95,
    agg: str = "mean",
    title: Optional[str] = None,
):
    """Grouped bar chart with error bars (CI by normal approx)."""
    set_style()
    grouped = df.groupby(group_col)[value_col]
    means = grouped.mean()
    counts = grouped.count()
    stds = grouped.std(ddof=1)
    # Normal approximation CI
    try:
        from scipy.stats import norm
        z = float(norm.ppf(0.5 + ci / 2.0))
    except Exception:
        # Fallback to standard normal z for 95% CI if SciPy not installed
        z = 1.96 if abs(ci - 0.95) < 1e-6 else 1.96
    se = stds / np.sqrt(counts)
    ci_half = z * se

    ax = means.plot(kind="bar", yerr=ci_half, capsize=5, color="#64B5F6")
    ax.set_ylabel(value_col)
    ax.set_xlabel(group_col)
    if title:
        ax.set_title(title)
    plt.tight_layout()
    return ax


def confusion_matrix_plot(cm: np.ndarray, class_names: Tuple[str, str] = ("Negative", "Positive"), title: str = "Confusion Matrix"):
    set_style()
    ax = sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                     xticklabels=class_names, yticklabels=class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    plt.tight_layout()
    return ax


def learning_curve_plot(estimator, X, y, cv=5, scoring=None, train_sizes=np.linspace(0.1, 1.0, 5)):
    if learning_curve is None:
        warnings.warn("sklearn not available for learning_curve; skipping.")
        return None
    set_style()
    sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, scoring=scoring, train_sizes=train_sizes, n_jobs=None, shuffle=True, random_state=42
    )
    train_mean = train_scores.mean(axis=1)
    test_mean = test_scores.mean(axis=1)
    plt.plot(sizes, train_mean, "o-", label="Train")
    plt.plot(sizes, test_mean, "o-", label="CV")
    plt.xlabel("Training examples")
    plt.ylabel(scoring or "Score")
    plt.title("Learning Curve")
    plt.legend()
    plt.tight_layout()
    return plt.gca()


def validation_curve_plot(estimator, X, y, param_name: str, param_range: Iterable, cv=5, scoring=None):
    if validation_curve is None:
        warnings.warn("sklearn not available for validation_curve; skipping.")
        return None
    set_style()
    train_scores, test_scores = validation_curve(
        estimator, X, y, param_name=param_name, param_range=param_range, cv=cv, scoring=scoring, n_jobs=None
    )
    train_mean = train_scores.mean(axis=1)
    test_mean = test_scores.mean(axis=1)
    plt.semilogx(param_range, train_mean, "o-", label="Train")
    plt.semilogx(param_range, test_mean, "o-", label="CV")
    plt.xlabel(param_name)
    plt.ylabel(scoring or "Score")
    plt.title("Validation Curve")
    plt.legend()
    plt.tight_layout()
    return plt.gca()


def wordcloud_from_series(series: pd.Series, max_words: int = 100):
    """Generate a word cloud from a pandas Series of text. Falls back to frequency bar chart if wordcloud not installed."""
    set_style()
    try:
        from wordcloud import WordCloud, STOPWORDS
        text = " ".join(series.dropna().astype(str))
        wc = WordCloud(width=800, height=400, max_words=max_words, background_color="white",
                       stopwords=STOPWORDS | {"the", "and", "to", "of", "in", "for"}).generate(text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud")
        plt.tight_layout()
        return plt.gca()
    except Exception:
        # Fallback: simple frequency bar chart
        from collections import Counter
        import re
        tokens = []
        for t in series.dropna().astype(str):
            tokens.extend([w.lower() for w in re.findall(r"[A-Za-z']+", t)])
        stop = {"the", "and", "to", "of", "in", "for", "a", "is", "on", "with", "it", "this", "that"}
        words = [w for w in tokens if w not in stop and len(w) > 2]
        top = Counter(words).most_common(20)
        if not top:
            plt.text(0.5, 0.5, "No words to display", ha="center")
            plt.axis("off")
            return plt.gca()
        labels, counts = zip(*top)
        sns.barplot(x=list(counts), y=list(labels), orient="h", color="#81C784")
        plt.title("Top Words (fallback)")
        plt.xlabel("Count")
        plt.ylabel("")
        plt.tight_layout()
        return plt.gca()
