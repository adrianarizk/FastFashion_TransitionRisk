import pandas as pd
import numpy as np
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/true_cost_fast_fashion.csv")
PROCESSED_DATA_PATH = Path("data/processed/clean_fast_fashion_emissions.csv")


def load_data(path: Path) -> pd.DataFrame:
    """
    Load raw fast fashion emissions dataset.
    """
    df = pd.read_csv(path)
    return df


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names for consistency.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values:
    - Drop rows missing critical identifiers
    - Impute numeric emissions-related values with median
    """
    critical_cols = ["brand", "country", "year"]
    df = df.dropna(subset=critical_cols)

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    return df


def convert_units(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure carbon emissions are expressed in metric tons of CO2 equivalent (tCO2e).
    If emissions are reported in kilograms, convert to tons.
    """
    if "carbon_emissions_kgco2e" in df.columns:
        df["carbon_emissions_tco2e"] = df["carbon_emissions_kgco2e"] / 1000
    return df


def remove_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove extreme outliers using the IQR method.
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df


def process_data() -> pd.DataFrame:
    """
    Full data processing pipeline.
    """
    df = load_data(RAW_DATA_PATH)
    df = clean_columns(df)
    df = handle_missing_values(df)
    df = convert_units(df)

    if "carbon_emissions_tco2e" in df.columns:
        df = remove_outliers(df, "carbon_emissions_tco2e")

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    return df


if __name__ == "__main__":
    process_data()

