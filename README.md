# Fast Fashion transition risk, Sustainability Consultants

This repository contains the analytical pipeline developed for a Green Finance / Sustainability project focused on assessing transition risk in the fast fashion industry.

The analysis quantifies brand-level carbon emissions and translates them into potential financial exposure under different carbon pricing scenarios.

---

## Project Structure
FastFashion_TransitionRisk/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_processing.py
│   └── emission_cost.py
├── notebooks/
│   └── debug_pipeline.ipynb
├── main.py
├── requirements.txt
└── README.md


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


