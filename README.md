# Data Quality Monitoring Pipeline

A lightweight data quality framework that profiles a CSV dataset, runs validation rules, and writes a machine-readable quality report.

## Checks

- Duplicate record IDs
- Missing customer IDs
- Negative income values
- Invalid age values

## Output

The pipeline creates `output/quality_report.json` containing:

- Dataset statistics
- Missing value counts
- Validation results
- Overall PASS or REVIEW status

## Run locally

```bash
pip install -r requirements.txt
python src/monitor.py
pytest
```

## Why this project matters

Data pipelines are only useful when downstream users can trust their data. This project demonstrates a simple approach to catching common data quality problems before analysis or modelling.

## Tech stack

Python, Pandas, JSON, Pytest

## Dataset

The dataset is synthetic. Data quality issues are intentionally injected so the monitoring checks can be demonstrated and tested.
