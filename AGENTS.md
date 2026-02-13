# AGENTS.md – AI-Based Detection of Hedge Fund Fraud

## Repository Purpose
Companion repository for the paper "AI-Based Detection of Hedge Fund Fraud: A Qualitative Survey" by Joerg Osterrieder. Contains Beamer teaching slides, self-assessment quizzes, and Python visualization scripts derived from the paper.

## Structure
- `paper/` — Full LaTeX source of the paper (8 sections + 3 appendices)
- `01_introduction/` through `08_reproducibility/` — Section slide decks, quizzes, and charts
- `A0_search_protocol/`, `A1_feature_engineering/`, `A2_glossary/` — Appendix materials
- `template_beamer_final.tex` — Shared Beamer template (Madrid theme, 16:9)
- `notation.tex` — Shared mathematical macros
- `charts.json` — Registry of all 21 visualization scripts

## Conventions
- Each section folder contains: slides (.tex), quiz (_quiz.tex), questions (questions.json), chart subfolders
- Charts: Python script → PDF output + thumb.png thumbnail
- Beamer template: Madrid theme, 8pt font, 16:9 aspect ratio, mlblue/mlpurple/mllavender colors
- CI: GitHub Actions for slide compilation, quiz validation, chart validation, link checking

## Key Numbers (keep consistent across all materials)
- $4.5 trillion AUM, 10.6% mean AUC degradation, 10 open problems
- 50–100 documented fraud cases, F1≈0.88 (tree ensembles)
- Search corpus: 500 initial → 120 screened → 80 core + 25 context = 105 systematic
- Survivorship bias: 242bp, Backfill bias: 442bp

## Paper Sections Mapping
| Folder | Paper Section | Topic |
|--------|--------------|-------|
| 01_introduction | §1 | Scale of fraud, why AI, contributions |
| 02_background | §2 | Fraud taxonomy, data ecosystem, regulation |
| 03_detection_pipeline | §3 | Five-stage detection pipeline (C1) |
| 04_literature_review | §4 | ML methods by family |
| 05_adversarial_regulatory | §5 | Adversarial robustness, EU AI Act (C2) |
| 06_research_agenda | §6 | 10 open problems (C3) |
| 07_conclusion | §7 | Synthesis and implications |
| 08_reproducibility | §8 | Reproducibility statement |
| A0_search_protocol | App A | SALSA methodology, search queries |
| A1_feature_engineering | App B | Feature engineering compendium |
| A2_glossary | App C | Glossary of terms |
