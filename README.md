# AlphaCare Insurance Risk Analytics

An end-to-end data science and analytics pipeline designed to analyze historical insurance claim data, optimize marketing strategy, and identify low-risk customer segments for AlphaCare Insurance Solutions.

## 📊 Project Overview
This repository contains the exploratory data analysis (EDA) framework and data engineering practices built for Task 1 and Task 2 of the interim milestone. The core objective is to calculate underwriting KPIs (Loss Ratios, Profit Margins) across geographical and demographic categories to spot optimization opportunities.

## 📂 Project Structure
```text
insurance-risk-analytics/
│
├── data/
│   ├── insurance_data.csv       # Raw historical dataset (git-ignored)
│   └── insurance_data.csv.dvc   # Data Version Control tracker file
│
├── notebooks/
│   └── 01_eda.ipynb            # Core analysis, calculations, and plotting panels
│
├── src/
│   ├── __init__.py             # Makes src importable as a module
│   ├── data_loader.py          # Safe, robust custom dataset loading pipeline
│   └── eda_utils.py            # Reusable styling and custom visualization functions
│
├── .gitignore                  # Production-ready file exclusion configuration
└── README.md                   # Project documentation (You are here!)
