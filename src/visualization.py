from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RANK_COST_PATH = Path("data/processed/toscane_rank_cost100.csv")
BRAND_ESG_PATH = Path("data/processed/toscane_brand_esg_summary.csv")

FIG_DIR = Path("figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)


def plot_brand_carbon_cost_ranking():
    df = pd.read_csv(RANK_COST_PATH)

    plt.figure()
    plt.bar(df["brand"], df["avg_cost_100eur"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Avg annual carbon cost (€) at 100 €/tCO2e")
    plt.title("Brand carbon cost exposure (100 €/tCO2e)")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "brand_carbon_cost_ranking.png", dpi=300)
    plt.close()


def plot_emissions_vs_gdp_efficiency():
    df = pd.read_csv(BRAND_ESG_PATH)

    plt.figure()
    plt.bar(df["brand"], df["efficiency_tco2e_per_gdp_musd"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("tCO2e per $1M GDP (lower = better)")
    plt.title("Emissions intensity relative to GDP contribution")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "emissions_vs_gdp.png", dpi=300)
    plt.close()


def generate_all_figures():
    plot_brand_carbon_cost_ranking()
    plot_emissions_vs_gdp_efficiency()
    print("[SUCCESS] Figures generated in /figures:")
    print(" - figures/brand_carbon_cost_ranking.png")
    print(" - figures/emissions_vs_gdp.png")


if __name__ == "__main__":
    generate_all_figures()