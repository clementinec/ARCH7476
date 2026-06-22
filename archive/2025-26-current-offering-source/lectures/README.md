# Lecture Slides

## ML to Python Overview Slides

### Quick Start

To render the slides:

```bash
cd /Users/guo/tprojs/ARCH7476/lectures
quarto render ml-to-python-overview.qmd
```

To preview with live reload:

```bash
quarto preview ml-to-python-overview.qmd
```

### Before You Present

**IMPORTANT**: Update these placeholder links in `ml-to-python-overview.qmd`:

1. **Google Drive Link** (slide "Where to Find Everything"):
   - Search for: `INSERT GOOGLE DRIVE LINK HERE`
   - Replace `https://drive.google.com/placeholder` with your actual Drive folder URL

2. **Feedback Form Link** (slide "Anonymous Feedback"):
   - Search for: `INSERT FEEDBACK FORM LINK HERE`
   - Replace `https://forms.google.com/placeholder` with your actual Google Form URL

### Customization Tips

- **Colors**: Edit `custom.scss` to change the color scheme
- **Transitions**: Change `transition: slide` in the YAML header to `fade`, `zoom`, `convex`, etc.
- **Slide numbers**: Remove `slide-number: true` to hide slide numbers
- **Incremental bullets**: Add `{.incremental}` to any list to make it reveal item by item
- **Two-column layouts**: Use the `:::{.columns}` syntax (see examples in slides)

### Speaker Notes

To add speaker notes that only you see, add this after any slide content:

```markdown
::: {.notes}
Remember to mention the office hours!
:::
```

### Export to PDF

```bash
quarto render ml-to-python-overview.qmd --to pdf
```

Or use "Print to PDF" from your browser in the rendered HTML version.

### Useful Shortcuts During Presentation

- `F` — Full screen
- `S` — Speaker view (shows notes and next slide)
- `O` — Overview mode (see all slides at once)
- `B` — Blank screen (black)
- `?` — Show keyboard shortcuts
- `C` — Toggle chalkboard (drawing mode)

### Structure Overview

The slide deck includes:

1. **Course Context** — Situates this lecture in the semester arc
2. **ML Primer Recap** — Summarizes key concepts from the PDF reading
3. **Python Practical** — Introduces the two notebooks
4. **Making It Yours** — Connects to student A3/A4 projects
5. **Resources & Next Steps** — Drive links, practice suggestions
6. **Wrap-Up & Feedback** — Q&A and anonymous survey

Total: ~40-50 minutes with live demo
