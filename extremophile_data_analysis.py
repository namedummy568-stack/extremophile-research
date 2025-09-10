
import pandas as pd
import numpy as np

def analyze_growth_curve(file_path):
    """
    Analyzes microbial growth curve data from a CSV file.
    Assumes the CSV has 'Time (hours)' and 'Optical Density (OD600)' columns.
    """
    df = pd.read_csv(file_path)
    
    print("Growth Curve Analysis:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())

    # Basic growth rate calculation (example: change in OD600 per hour)
    if len(df) > 1:
        time_diff = df['Time (hours)'].diff().iloc[1]
        od_diff = df['Optical Density (OD600)'].diff().iloc[1]
        if time_diff > 0:
            growth_rate = od_diff / time_diff
            print(f"\nApproximate initial growth rate (OD600/hour): {growth_rate:.4f}")
        else:
            print("\nCannot calculate growth rate: Insufficient time difference.")
    else:
        print("\nCannot calculate growth rate: Not enough data points.")

if __name__ == "__main__":
    # Example usage:
    # analyze_growth_curve('experiment_results_strain_X.csv')
    pass
