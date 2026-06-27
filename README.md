# Two-Page Cheating Paper Skill

Codex skill for turning course notes, PDFs, slides, pasted text, and draft LaTeX/Markdown into an exactly two-page printable exam cheating paper.

This skill was distilled from an information-theory four-column cheat sheet workflow:

- A4 landscape, four columns, double-sided / exactly two rendered pages
- dense formula-first Chinese note style
- blue compact section labels
- real LaTeX math instead of rasterized formulas
- TikZ or source-slide diagrams only when they improve exam recall
- strict page-count validation before handoff

## Install

Copy this directory into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
cp -R two-page-cheating-paper-skill ~/.codex/skills/two-page-cheating-paper
```

Or clone this repository directly into the skills folder:

```bash
git clone <repo-url> ~/.codex/skills/two-page-cheating-paper
```

## Use

Mention the skill in Codex:

```text
$two-page-cheating-paper 根据这些笔记生成一份两页 A4 正反面速查表
```

The skill treats the rendered PDF page count as a hard contract. It compiles, counts pages, and keeps fitting until the output is exactly two pages.

## Contents

- `SKILL.md`: skill trigger, workflow, quality gate, and handoff rules
- `references/layout-contract.md`: LaTeX layout contract and fitting ladder
- `scripts/check_pdf_pages.py`: page-count checker for compiled PDFs
- `agents/openai.yaml`: model routing preference for high-context document compression

## Validation

Run:

```bash
python3 scripts/check_pdf_pages.py path/to/output.pdf --expect 2
```

The script exits nonzero unless the PDF has exactly two pages.
