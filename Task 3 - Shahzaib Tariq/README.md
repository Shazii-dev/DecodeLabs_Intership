# Tech Stack Recommender

A simple content-based filtering recommender built in Python using `pandas` and `scikit-learn`.

## Overview

This repo implements a 4-step Input-Process-Output (IPO) pipeline:

1. Ingestion: validate a user profile with a minimum of 3 skills.
2. Scoring: map text to TF-IDF vectors and compute cosine similarity.
3. Sorting: order job roles by similarity descending.
4. Filtering: return the top N recommended job roles.

A cold-start fallback also returns a trending list when the user provides zero skills.

## Files

- `tech_stack_recommender.py`: main Python script
- `README.md`: usage instructions

## Requirements

- Python 3.9+
- pandas
- scikit-learn

## Install

```bash
pip install pandas scikit-learn
```

## Run

```bash
python tech_stack_recommender.py
```

## Behavior

- Standard user input example runs with `['Python', 'Cloud Computing', 'Automation']`
- Cold start example runs when input is `[]`

## Notes

- The dataset is mocked in code and simulates `raw_skills.csv`.
- TF-IDF is used to penalize generic terms and reward specific matching skills.
- Cosine similarity is used for orientation/alignment scoring.
