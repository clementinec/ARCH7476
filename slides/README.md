# Course-intro slide deck (LaTeX Beamer)

`course-intro.tex` — 18-frame, 10–20 minute introduction to ARCH7476 for the
mixed cohort (MArch primary audience). Metropolis theme, 16:9.

## Build

```sh
xelatex course-intro.tex   # run twice for the progress bar / outlines
```

Requires XeLaTeX (TeX Live with the `metropolis` Beamer theme). Fira fonts are
loaded straight from the TeX tree via an explicit `Path=` in the preamble — if
you upgrade TeX Live, update that path (search for `texlive/2023` in the .tex).
The Kai Tak photo credit uses the macOS system font *PingFang HK*; on another
OS, swap the `\newfontfamily\cjkfont` line for any CJK font you have.

## Content sources

Everything on the slides is drawn from the current course materials
(`index.qmd`, `schedule.qmd`, `assignments/*.qmd`, `weeks/week-*.qmd`,
`resources.qmd`). The gamified `*-engaging.qmd` decks and
`week-04-speaker-notes.md` are legacy material from the earlier offering,
deliberately **not** used, and now live in `archive/legacy-2025/`.

Images are referenced relative to the repo root (`\graphicspath{{../}}`):

- `assets/examples/*.jpg` — four CC-licensed case photos (credits on slides,
  full records in `assets/examples/sources.csv`)
- `assets/02MC.png` — instructor's PMV-vs-TSV figure (own work)

## Not tracked

`*.aux/log/nav/out/snm/toc` and the PDF are build artifacts; regenerate with
the command above.
