# ML_FINAL_PROJECT_2026
# ML Final Project 2026

This project is focused on the analysis of football player data. The main goal is to explore the dataset, understand the most important player characteristics, perform feature engineering, build machine learning models, and evaluate their performance.

The dataset contains information about football players, including age, height, weight, nationality, positions, overall rating, market value, wage, technical skills, and other performance-related attributes.

## Project Structure

```text
ML_FINAL_PROJECT_2026/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── artifacts/
│   ├── logs/
│   └── saved_models/
│
├── notebooks/
│   ├── 01_overview.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling.ipynb
│   └── 05_evaluation.ipynb
│
├── reports/
│   └── figures/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── utils/
│   └── visualization/
│
└── README.md
```

## Folder Description

### `data/`

This folder contains the project datasets.

* `data/raw/` stores the original dataset without modifications.
* `data/processed/` stores cleaned or transformed datasets created during preprocessing and feature engineering.

### `models/`

This folder stores files related to machine learning models.

* `models/saved_models/` contains trained machine learning models.
* `models/artifacts/` contains supporting files such as encoders, scalers, or model outputs.
* `models/logs/` contains logs and experiment information from the training process.

### `notebooks/`

This folder contains the Jupyter notebooks used during the project development.

* `01_overview.ipynb` provides an initial overview of the dataset.
* `02_eda.ipynb` contains exploratory data analysis and visualizations.
* `03_feature_engineering.ipynb` contains preprocessing and feature creation.
* `04_modeling.ipynb` contains model training.
* `05_evaluation.ipynb` contains model evaluation and comparison.

### `reports/`

This folder stores generated reports and visual outputs.

* `reports/figures/` contains saved charts and visualizations used in the analysis and final report.

### `src/`

This folder contains reusable Python source code for the project.

* `src/data/` contains functions for loading and preparing data.
* `src/features/` contains functions for feature engineering.
* `src/models/` contains functions for model training, prediction, and evaluation.
* `src/utils/` contains helper functions used across the project.
* `src/visualization/` contains functions for creating and saving plots.

## Project Workflow

The project follows a structured machine learning workflow:

1. Load and inspect the dataset.
2. Perform an initial data overview.
3. Explore the data through visualizations and statistical analysis.
4. Clean and preprocess the data.
5. Create new useful features.
6. Train machine learning models.
7. Evaluate and compare model performance.
8. Save important figures, reports, and model artifacts.

## Goal

The goal of this project is to build a complete and well-structured machine learning workflow using football player data. 

