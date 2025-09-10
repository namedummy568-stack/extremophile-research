
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

def calculate_doubling_time(df, initial_od, final_od, time_col='Time (hours)', od_col='Optical Density (OD600)'):
    """
    Calculates the doubling time from growth curve data.
    Assumes exponential growth between initial_od and final_od.
    """
    df_filtered = df[(df[od_col] >= initial_od) & (df[od_col] <= final_od)]
    if len(df_filtered) < 2:
        return None

    # Fit a linear regression to the natural log of OD values
    df_filtered['ln_OD'] = np.log(df_filtered[od_col])
    
    # Simple linear regression for growth rate (k)
    # k = (ln(OD2) - ln(OD1)) / (t2 - t1)
    # Doubling time (td) = ln(2) / k

    # Using the first and last points of the filtered data for simplicity
    t1 = df_filtered[time_col].iloc[0]
    t2 = df_filtered[time_col].iloc[-1]
    od1 = df_filtered[od_col].iloc[0]
    od2 = df_filtered[od_col].iloc[-1]

    if od1 <= 0 or od2 <= 0 or t2 == t1:
        return None

    k = (np.log(od2) - np.log(od1)) / (t2 - t1)
    if k <= 0:
        return None # No growth or decline

    doubling_time = np.log(2) / k
    return doubling_time

if __name__ == "__main__":
    # Example usage:
    # analyze_growth_curve('experiment_results_strain_X.csv')
    pass
