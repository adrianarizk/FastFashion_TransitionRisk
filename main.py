from src.data_processing import process_data
from src.emission_cost import generate_emissions_cost_table


def main():
    """
    Run full fast fashion emissions and carbon cost analysis pipeline.
    """
    print("Starting data processing...")
    process_data()

    print("Computing emissions and carbon costs...")
    generate_emissions_cost_table()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()

