---
name: two-page-cheating-paper
description: Generate exactly two rendered pages of dense printable exam cheating paper from notes, pasted text, PDFs, slides, existing study notes, or draft LaTeX/Markdown. Use when the user asks for a cheating paper, cheat sheet, 速查表, 小抄, formula sheet, A4 double-sided sheet, 正反面一张纸, or asks to compress course notes into a LaTeX/PDF sheet whose final rendered output must be exactly 2 pages.
---

# Two-Page Cheating Paper

## Non-negotiable contract

Deliver a final artifact only after the rendered PDF has exactly two pages. Treat page count as a hard validation gate, not a preference.

Use `scripts/check_pdf_pages.py` after every compile. If the count is not exactly `2`, keep fitting:

- `0-1 pages`: add high-value missing material, enlarge images, or relax compression slightly.
- `3+ pages`: compress wording, remove low-yield examples, reduce vertical spacing, reduce image size, or move prose into formulas/templates.
- `2 pages`: still visually inspect rendered PNGs before final handoff.

## Workflow

1. Collect constraints.
   - Confirm whether the sheet must be A4 portrait or landscape. Default to A4 landscape, four columns, two pages.
   - Preserve explicit exclusions. If the user says a topic does not test, do not re-add it while comparing references.
   - Prefer LaTeX/PDF when formulas matter. Do not rasterize formulas unless explicitly requested.

2. Ingest notes and source materials.
   - For PDFs/slides, extract text and render pages for visual review because formula extraction can be lossy.
   - For existing notes, build a topic inventory first: definitions, theorem names, formulas, conditions, proof skeletons, algorithms, standard examples, and common mistakes.
   - For reference sheets, compare by coverage and exam utility, not raw word count.

3. Compress into exam-useful content.
   - Use compact blocks: definition -> formula -> condition/equality -> use case -> common trap.
   - Prefer formulas and short Chinese explanations over long prose.
   - Keep notation consistent. State log base and units once.
   - Group related formulas together; e.g. entropy/KL/MI chain rules in one block.
   - When notes contain worked examples, keep only examples that encode a reusable exam pattern.

4. Build the LaTeX sheet.
   - Read `references/layout-contract.md` before writing a new `.tex` file or repairing layout.
   - Start from `templates/two-page-cheating-paper.tex` when creating a new sheet.
   - Use the two-page layout contract, not a normal article template.
   - Keep source editable. Use TikZ for simple diagrams and real LaTeX math for formulas.
   - Put reusable figures in `latex_build/image/`; use stable relative paths.

5. Compile, count, render, inspect.
   - Compile with XeLaTeX.
   - Run `scripts/check_pdf_pages.py <pdf> --expect 2`.
   - Render both pages to PNG and inspect for clipping, unreadable formulas, stray characters, column overflow, and bad image alignment.
   - Do not claim completion until the PDF is exactly 2 pages and visually acceptable.

6. Fit using the compression ladder.
   - First remove duplicated prose and repeated theorem explanations.
   - Then tune local spacing and image sizes.
   - Then reduce font size or line height slightly.
   - Last resort: cut optional examples, historical notes, or topics explicitly marked non-exam.
   - Avoid shrinking so far that formulas become unreadable.

## Content style based on the reference information-theory sheet

Use the structure and density of the existing information-theory cheating paper as the model:

- Four columns on A4 landscape.
- Blue compact section labels.
- Formula-heavy, short explanation text.
- Important diagrams only when they save space or clarify relationships.
- Channel/graph diagrams paired with concrete analysis beside the figure.
- Algorithms compressed as step rules, not paragraphs.
- Proofs as skeletons: assumptions -> key inequality -> conclusion.

## Handoff

Return links to:

- the editable `.tex`;
- the compiled `.pdf`;
- any image folder if figures are used.

Also state whether the PDF page-count check passed exactly `2/2`.
