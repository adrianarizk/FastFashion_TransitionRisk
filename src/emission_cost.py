import pandas as pd
from pathlib import Path


PROCESSED_DATA_PATH = Path("data/processed/clean_fast_fashion_emissions.csv")
OUTPUT_DATA_PATH = Path("data/processed/brand_country_year_emissions_costs.csv")


CARBON_PRICE_SCENARIOS = {
    "cost_low_eur": 50,
    "cost_mid_eur": 100,
    "cost_high_eur": 150,
}


def load_clean_data(path: Path) -> pd.DataFrame:
    """
    Load cleaned emissions dataset.
    """
    return pd.read_csv(path)


def aggregate_emissions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total yearly emissions at Brand × Country × Year level.
    """
    grouped = (
        df.groupby(["brand", "country", "year"], as_index=False)
          .agg({"carbon_emissions_tco2e": "sum"})
    )
    return grouped


def compute_carbon_costs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute carbon costs under different carbon price scenarios.
    """
    for col_name, price in CARBON_PRICE_SCENARIOS.items():
        df[col_name] = df["carbon_emissions_tco2e"] * price
    return df


def generate_emissions_cost_table() -> pd.DataFrame:
    """
    Full pipeline: load clean data, aggregate emissions, compute carbon costs.
    """
    df = load_clean_data(PROCESSED_DATA_PATH)
    df = aggregate_emissions(df)
    df = compute_carbon_costs(df)

    OUTPUT_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_DATA_PATH, index=False)

    return df


if __name__ == "__main__":
    generate_emissions_cost_table()

