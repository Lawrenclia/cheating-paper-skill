# Two-page LaTeX layout contract

Use this reference whenever the output must be exactly two rendered pages.

## Default page model

Use A4 landscape, four columns, two pages.

```tex
\documentclass[UTF8,a4paper,landscape,fontset=none]{ctexart}
\usepackage[left=0.3cm,right=0.3cm,top=0.3cm,bottom=0.3cm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc}
\setCJKmainfont{Songti SC}
\setCJKsansfont{Heiti SC}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\columnsep}{0.05cm}
\setlength{\columnseprule}{0pt}
\setlength{\emergencystretch}{1.5em}
\definecolor{keyblue}{HTML}{1476D4}
\newcommand{\chap}[1]{\par\textcolor{keyblue}{\sffamily\bfseries #1}\par}
\newcommand{\topic}[1]{\par\textcolor{keyblue}{\sffamily\bfseries #1}\par}
\newcommand{\tight}{\fontsize{6.5pt}{6.75pt}\selectfont}
```

Start the document:

```tex
\begin{document}
\tight
\raggedright
\begin{multicols*}{4}
% content
\end{multicols*}
\end{document}
```

If text looks vertically squashed, increase line height first:

```tex
\newcommand{\tight}{\fontsize{6.5pt}{7.1pt}\selectfont}
```

If content spills to page 3, compress before reducing below `6pt`.

## Figure macros

```tex
\graphicspath{{../}{./}}
\newcommand{\pptfig}[2][0.7]{%
  \par\vspace{0.35pt}\noindent
  \makebox[\linewidth][c]{\includegraphics[width=#1\linewidth]{#2}}%
  \par\vspace{0.35pt}%
}
```

Use call-site scaling:

```tex
\pptfig[0.58]{image/info_diagram.png}
```

## Side-by-side diagram card

Use for small conceptual diagrams such as channel capacity figures.

```tex
\newcommand{\chanfont}{\fontsize{4.75pt}{4.75pt}\selectfont}
\newcommand{\chcard}[3]{%
  \par\vspace{0.45pt}\noindent
  \begin{minipage}[t]{0.43\linewidth}
    \vspace{0pt}
    \centering #2\par
  \end{minipage}\hfill
  \begin{minipage}[t]{0.54\linewidth}
    \vspace{0pt}
    {\chanfont\sffamily\textcolor{keyblue}{#1}\par #3}
  \end{minipage}\par\vspace{0.45pt}%
}
```

Important: never write `\vspace{0pt};`. The semicolon renders as visible text before every diagram.

## Two-page fitting ladder

Use this order when the PDF is not exactly two pages:

1. Remove duplicated content.
2. Convert prose into formulas or rule fragments.
3. Merge adjacent related topics.
4. Shrink large images by 5-15%.
5. Remove optional examples and history.
6. Tighten `\parskip`, `\vspace`, and diagram card spacing.
7. Reduce line height slightly.
8. Reduce main font size only after the above.

If the result is only one page or visibly underfilled:

1. Add missing high-value topics from notes.
2. Add proof skeletons or equality conditions.
3. Add small clarifying diagrams.
4. Restore examples that encode reusable exam patterns.

## Content ordering pattern

For dense course notes, organize by exam retrieval:

1. Basic definitions and notation.
2. Core identities and chain rules.
3. Inequalities and equality conditions.
4. Theorems with achievability/converse skeletons.
5. Algorithms and construction steps.
6. Standard examples and capacity/formula tables.
7. Common mistakes and recognition heuristics.

## Visual QA checklist

Before final handoff:

- PDF has exactly two pages.
- No column text is clipped.
- Math glyphs render as text, not missing boxes.
- No stray punctuation before images.
- Images align with adjacent analysis text.
- CJK font is stable and readable.
- Page 2 does not overflow below the bottom edge.
