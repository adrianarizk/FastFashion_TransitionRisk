import os
import pandas as pd

# =====================================================
# TOSCANE – Sustainability Consultant Analysis
# Benchmarks, ESG efficiency, leaders & laggards
# =====================================================

COST_PATH = "data/processed/brand_country_year_emissions_costs.csv"
CLEAN_PATH = "data/processed/clean_fast_fashion_emissions.csv"
OUT_DIR = "data/processed"

def main():

    # -------------------------------------------------
    # 1) Load processed data
    # -------------------------------------------------
    cost = pd.read_csv(COST_PATH)
    clean = pd.read_csv(CLEAN_PATH)

    print("\n[INFO] Cost table head():")
    print(cost.head())

    print("\n[INFO] Clean table head():")
    print(clean.head())

    # -------------------------------------------------
    # 2) Ranking by emissions (average per brand)
    # -------------------------------------------------
    rank_emissions = (
        cost.groupby("brand")["carbon_emissions_tco2e"]
        .mean()
        .sort_values(ascending=False)
        .reset_index(name="avg_emissions_tco2e")
    )

    # -------------------------------------------------
    # 3) Ranking by carbon-cost exposure (€100 / tCO2e)
    # -------------------------------------------------
    rank_cost = (
        cost.groupby("brand")["cost_mid_eur"]
        .mean()
        .sort_values(ascending=False)
        .reset_index(name="avg_cost_100eur")
    )

    # -------------------------------------------------
    # 4) Build GDP + ESG table (brand-country-year)
    # -------------------------------------------------
    gdp_esg = (
        clean.groupby(["brand", "country", "year"], as_index=False)
        .agg({
            "gdp_contribution_million_usd": "sum",
            "sustainability_score": "mean",
            "ethical_rating": "mean",
            "transparency_index": "mean",
            "sentiment_score": "mean"
        })
    )

    # Merge cost table with GDP/ESG
    df_merged = cost.merge(
        gdp_esg,
        on=["brand", "country", "year"],
        how="left"
    )

    # -------------------------------------------------
    # 5) Efficiency KPI: emissions / GDP (lower = better)
    # -------------------------------------------------
    df_merged["efficiency_tco2e_per_gdp_musd"] = (
        df_merged["carbon_emissions_tco2e"]
        / df_merged["gdp_contribution_million_usd"]
    )

    rank_efficiency = (
        df_merged.groupby("brand")["efficiency_tco2e_per_gdp_musd"]
        .mean()
        .sort_values()
        .reset_index(name="avg_efficiency_tco2e_per_gdp_musd")
    )

    # -------------------------------------------------
    # 6) Brand-level ESG summary (for interpretation)
    # -------------------------------------------------
    brand_esg = (
        df_merged.groupby("brand")[[
            "carbon_emissions_tco2e",
            "sustainability_score",
            "ethical_rating",
            "transparency_index",
            "efficiency_tco2e_per_gdp_musd"
        ]]
        .mean()
        .sort_values("efficiency_tco2e_per_gdp_musd")
        .reset_index()
    )

    # -------------------------------------------------
    # 7) Display key results
    # -------------------------------------------------
    print("\n=== Ranking by emissions (avg) ===")
    print(rank_emissions)

    print("\n=== Ranking by carbon cost (€100/t, avg) ===")
    print(rank_cost)

    print("\n=== Ranking by efficiency (lower = better) ===")
    print(rank_efficiency)

    print("\n=== Brand ESG summary ===")
    print(brand_esg)

    # -------------------------------------------------
    # 8) Save outputs
    # -------------------------------------------------
    os.makedirs(OUT_DIR, exist_ok=True)

    rank_emissions.to_csv(
        f"{OUT_DIR}/toscane_rank_emissions.csv", index=False
    )
    rank_cost.to_csv(
        f"{OUT_DIR}/toscane_rank_cost100.csv", index=False
    )
    rank_efficiency.to_csv(
        f"{OUT_DIR}/toscane_rank_efficiency.csv", index=False
    )
    brand_esg.to_csv(
        f"{OUT_DIR}/toscane_brand_esg_summary.csv", index=False
    )

    print("\n[SUCCESS] Toscane outputs saved:")
    print(f" - {OUT_DIR}/toscane_rank_emissions.csv")
    print(f" - {OUT_DIR}/toscane_rank_cost100.csv")
    print(f" - {OUT_DIR}/toscane_rank_efficiency.csv")
    print(f" - {OUT_DIR}/toscane_brand_esg_summary.csv")


if __name__ == "__main__":
    main()
