# GitHub Workflows

This directory contains CI/CD workflows for the repository.

## Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| compile_slides.yml | Push/PR to .tex files | Compiles all Beamer slides |
| validate_quizzes.yml | Push/PR to questions.json | Validates quiz JSON schema |
| validate_charts.yml | Push/PR to .py files | Runs chart scripts |
| link-check.yml | Push/PR to .md files | Checks markdown links |
