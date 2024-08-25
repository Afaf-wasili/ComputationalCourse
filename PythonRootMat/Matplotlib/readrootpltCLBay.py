import os
import uproot
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

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

    # Print extracted data
    print("Data Histogram:")
    print("Edges:", data_edges)
    print("Values:", data_values)

    print("MC Histogram:")
    print("Edges:", mc_edges)
    print("Values:", mc_values)

    # Define prior parameters for Bayesian intervals
    prior_alpha = 0.1
    prior_beta = 0.1
    confidence_level = 0.95
    alpha = 1 - confidence_level

    def compute_bayesian_intervals(counts, prior_alpha, prior_beta, alpha):
        lower_bounds = []
        upper_bounds = []
        for count in counts:
            # Posterior parameters
            posterior_alpha = prior_alpha + count
            posterior_beta = prior_beta + 1

            # Compute intervals
            lower_bound = gamma.ppf(alpha / 2, a=posterior_alpha, scale=1 / posterior_beta)
            upper_bound = gamma.ppf(1 - alpha / 2, a=posterior_alpha, scale=1 / posterior_beta)

            lower_bounds.append(lower_bound)
            upper_bounds.append(upper_bound)

        return np.array(lower_bounds), np.array(upper_bounds)

    # Compute Bayesian intervals for data histogram
    data_lower_bounds, data_upper_bounds = compute_bayesian_intervals(data_values, prior_alpha, prior_beta, alpha)

    # Adjust Bayesian intervals to match histogram peak
    max_count = np.max(data_values)
    data_lower_bounds = np.clip(data_lower_bounds, 0, max_count)
    data_upper_bounds = np.clip(data_upper_bounds, 0, max_count)

    # Plot histograms
    plt.figure(figsize=(12, 10))

    # Data histogram
    plt.subplot(2, 1, 1)
    plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
    plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
    plt.xlabel('X axis')
    plt.ylabel('Counts')
    plt.title('Histograms from ROOT File')
    plt.legend()
    plt.grid(True)

    # Plot Bayesian Confidence Intervals
    plt.subplot(2, 1, 2)
    plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
    plt.fill_between(data_edges[:-1], data_lower_bounds, data_upper_bounds, color='blue', alpha=0.3, label='95% Bayesian CI')
    plt.xlabel('X axis')
    plt.ylabel('Counts')
    plt.title('Data with Bayesian Confidence Intervals')
    plt.legend()
    plt.grid(True)

    # Save plot
    plt.tight_layout()
    plt.savefig('Plots/histograms_with_bayesian_intervals.png')
    plt.show()
