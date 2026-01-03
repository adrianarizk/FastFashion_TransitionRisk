from src.data_processing import process_data
from src.emission_cost import generate_emissions_cost_table
from src.toscane_analysis import main as toscane_main
from src.visualization import generate_all_figures


def main():
    """
    Run full fast fashion emissions + carbon cost + consulting analysis pipeline,
    and generate the figures used in the report.
    """
    print("Starting data processing...")
    process_data()

    print("Computing emissions and carbon costs...")
    generate_emissions_cost_table()

    print("Running Toscane consulting analysis (rankings + ESG summary)...")
    toscane_main()

    print("Generating figures for the report...")
    generate_all_figures()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()