# Fast Fashion transition risk, Sustainability Consultants

This repository contains the analytical pipeline developed for a Green Finance / Sustainability project focused on assessing transition risk in the fast fashion industry.

The analysis quantifies brand-level carbon emissions and translates them into potential financial exposure under different carbon pricing scenarios.

---

## Project Structure

```
FastFashion_TransitionRisk/
├── data/
│   ├── raw/                     # Original fast fashion emissions dataset
│   └── processed/               # Cleaned and aggregated datasets (brand–country–year level)
│
├── figures/
│   ├── brand_carbon_cost_ranking.png   # Brand-level carbon cost exposure (€100/tCO₂e)
│   └── emissions_vs_gdp.png            # Carbon efficiency by brand (tCO₂e per $1M GDP)
│
├── report/
│   └── Research_project_report.pdf     # Final written research report
│
├── slides/
│   └── Fastfashion-Researchproject.pdf # Project presentation slides
│
├── src/
│   ├── data_processing.py        # Data cleaning, standardization, and preprocessing
│   ├── emission_cost.py          # Emissions aggregation and carbon cost computation
│   ├── toscane_analysis.py       # Brand-level ESG and transition risk analysis
│   └── visualization.py          # Figures and visual outputs generation
│
├── main.py                       # Single entry point to reproduce the full analysis
├── requirements.txt              # Python dependencies for reproducibility
├── README.md                     # Project documentation
└── .gitignore
```

---

## Methodology Overview

1. Raw emissions data are cleaned and standardized (column harmonization, missing values, unit consistency, outlier checks).
2. Annual carbon emissions are aggregated at the brand–country–year level.
3. Carbon cost exposure is computed under three pricing scenarios:
   - €50 / tCO₂e (low)
   - €100 / tCO₂e (central)
   - €150 / tCO₂e (high)

The resulting outputs support transition risk assessment and sustainability advisory analysis.

---

## How to Run the Analysis

From the project root:

```bash
pip install -r requirements.txt
python main.py



