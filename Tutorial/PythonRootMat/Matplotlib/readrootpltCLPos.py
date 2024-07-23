import os
import uproot
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

file_path = "Plots/histo.root"

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"The file {file_path} does not exist. Please check the path.")
else:
    # Open the ROOT file
    file = uproot.open(file_path)

    # Access histograms
    data_hist = file["data"]
    mc_hist = file["MC"]

    # Extract data
    data_edges = data_hist.axis().edges()
    data_values = data_hist.values()
    mc_edges = mc_hist.axis().edges()
    mc_values = mc_hist.values()

    # Ensure edges are the same for data and MC
    if not np.array_equal(data_edges, mc_edges):
        print("Warning: The edges of the data and MC histograms do not match. Please check the histograms.")

    # Function to calculate Poisson confidence intervals manually
    def poisson_confidence_interval(counts, confidence=0.95):
        lower_bound = np.zeros_like(counts, dtype=float)
        upper_bound = np.zeros_like(counts, dtype=float)
        z = norm.ppf(1 - (1 - confidence) / 2)
        for i, count in enumerate(counts):
            if count > 0:
                # Approximate method for confidence intervals for Poisson distribution
                lower_bound[i] = max(0, count - z * np.sqrt(count))
                upper_bound[i] = count + z * np.sqrt(count)
            else:
                lower_bound[i] = 0
                upper_bound[i] = 0
        return lower_bound, upper_bound

    # Calculate confidence intervals for data
    data_lower, data_upper = poisson_confidence_interval(data_values, confidence=0.95)

    # Plot Data Histogram with Confidence Levels
    plt.figure(figsize=(10, 7))
    plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
    plt.fill_between(data_edges[:-1], data_lower, data_upper, color='blue', alpha=0.2, label='95% CL')
    plt.xlabel('X axis')
    plt.ylabel('Counts')
    plt.title('Data Histogram with Confidence Levels')
    plt.legend()
    plt.grid(True)
    plt.savefig('Plots/data_histogram_with_CL_Pos.png')
    plt.close()

    # Calculate ratio of data to MC
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = np.divide(data_values, mc_values, out=np.zeros_like(data_values), where=mc_values != 0)
        ratio_error = np.sqrt(np.divide(data_values, mc_values**2, out=np.zeros_like(mc_values), where=mc_values != 0))

    # Plot Ratio of Data to MC
    plt.figure(figsize=(10, 7))
    plt.errorbar(data_edges[:-1] + (data_edges[1] - data_edges[0]) / 2, ratio, yerr=ratio_error, fmt='o', color='black', label='Data/MC Ratio')
    
    # Highlight ±1σ and ±2σ regions
    plt.axhline(y=1, color='gray', linestyle='--', label='Ratio = 1')
    plt.fill_between(data_edges[:-1], 1 - ratio_error, 1 + ratio_error, color='green', alpha=0.3, label='±1σ')
    plt.fill_between(data_edges[:-1], 1 - 2*ratio_error, 1 + 2*ratio_error, color='orange', alpha=0.2, label='±2σ')
    
    plt.xlabel('X axis')
    plt.ylabel('Data/MC Ratio')
    plt.title('Ratio of Data to MC with ±1σ and ±2σ')
    plt.legend()
    plt.grid(True)
    plt.savefig('Plots/data_mc_ratio_with_errors.png')
    plt.close()
