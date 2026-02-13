# AI-Based Detection of Hedge Fund Fraud

**A Systematic Survey and Research Agenda**

[![Compile Slides](https://github.com/Digital-AI-Finance/ai-based-detection-hedge-fund-fraud/actions/workflows/compile_slides.yml/badge.svg)](https://github.com/Digital-AI-Finance/ai-based-detection-hedge-fund-fraud/actions/workflows/compile_slides.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository showcases the paper **"AI-Based Detection of Hedge Fund Fraud: A Systematic Survey and Research Agenda"** by Joerg Osterrieder (Zurich University of Applied Sciences). The paper addresses a critical gap in the literature by providing the first systematic, hedge-fund-specific framework for AI-based fraud detection.

### Key Numbers

| Metric | Value |
|--------|-------|
| Hedge fund AUM | $4.5 trillion |
| Mean AUC degradation under adversarial attack | 10.6% |
| Open research problems identified | 10 |
| Documented fraud cases available | 50--100 |
| Systematic literature corpus | 105 papers |

### Three Contributions

1. **C1: Detection Pipeline Taxonomy** -- A unified five-stage framework (data ingestion, feature engineering, model selection, explainability, deployment) mapping fraud types to AI methods
2. **C2: Adversarial and Regulatory Readiness** -- Assessment of method robustness under adversarial attack and compliance with EU AI Act / SEC requirements
3. **C3: Research Roadmap** -- Ten concrete open problems spanning data, methodology, and deployment challenges

## Repository Structure

| Section | Topic | Slides | Quiz | Charts |
|---------|-------|--------|------|--------|
| 01 | Introduction | [Slides](01_introduction/01_introduction.tex) | [Quiz](01_introduction/01_introduction_quiz.tex) | 2 |
| 02 | Background | [Slides](02_background/02_background.tex) | [Quiz](02_background/02_background_quiz.tex) | 3 |
| 03 | Detection Pipeline (C1) | [Slides](03_detection_pipeline/03_detection_pipeline.tex) | [Quiz](03_detection_pipeline/03_detection_pipeline_quiz.tex) | 3 |
| 04 | Literature Review | [Slides](04_literature_review/04_literature_review.tex) | [Quiz](04_literature_review/04_literature_review_quiz.tex) | 2 |
| 05 | Adversarial & Regulatory (C2) | [Slides](05_adversarial_regulatory/05_adversarial_regulatory.tex) | [Quiz](05_adversarial_regulatory/05_adversarial_regulatory_quiz.tex) | 3 |
| 06 | Research Agenda (C3) | [Slides](06_research_agenda/06_research_agenda.tex) | [Quiz](06_research_agenda/06_research_agenda_quiz.tex) | 2 |
| 07 | Conclusion | [Slides](07_conclusion/07_conclusion.tex) | [Quiz](07_conclusion/07_conclusion_quiz.tex) | 2 |
| 08 | Reproducibility | [Slides](08_reproducibility/08_reproducibility.tex) | [Quiz](08_reproducibility/08_reproducibility_quiz.tex) | 2 |
| A0 | Search Protocol | [Slides](A0_search_protocol/A0_search_protocol.tex) | [Quiz](A0_search_protocol/A0_search_protocol_quiz.tex) | 1 |
| A1 | Feature Engineering | [Slides](A1_feature_engineering/A1_feature_engineering.tex) | [Quiz](A1_feature_engineering/A1_feature_engineering_quiz.tex) | 1 |
| A2 | Glossary | [Slides](A2_glossary/A2_glossary.tex) | -- | -- |

## Technical Details

- **Format**: Beamer slides (Madrid theme, 8pt, 16:9)
- **Charts**: Standalone Python scripts generating PDF outputs
- **Paper**: Full LaTeX source in `paper/` directory

## Folder Structure

```
ai-based-detection-hedge-fund-fraud/
├── 01_introduction/          # Section slides + quiz + charts
├── 02_background/
├── 03_detection_pipeline/
├── ...
├── A0_search_protocol/       # Appendix slides
├── A1_feature_engineering/
├── A2_glossary/
├── paper/                    # Full paper LaTeX source
├── template_beamer_final.tex # Shared Beamer template
├── notation.tex              # Shared notation macros
└── README.md
```

## Requirements

- Python 3.8+ with matplotlib, numpy, seaborn
- LaTeX distribution with Beamer support

## Installation

```bash
git clone https://github.com/Digital-AI-Finance/ai-based-detection-hedge-fund-fraud.git
cd ai-based-detection-hedge-fund-fraud
pip install -r requirements.txt
```

## Citation

```bibtex
@article{osterrieder2025hedge,
  title={AI-Based Detection of Hedge Fund Fraud: A Systematic Survey and Research Agenda},
  author={Osterrieder, Joerg},
  year={2025},
  institution={Zurich University of Applied Sciences}
}
```

## License

MIT License

---

(c) Joerg Osterrieder 2025
