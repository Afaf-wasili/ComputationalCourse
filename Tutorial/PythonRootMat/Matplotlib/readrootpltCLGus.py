import uproot
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

file_path = "Plots/histo.root"

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

# Calculate Gaussian confidence intervals
def gaussian_confidence_interval(counts, confidence=0.95):
    z = norm.ppf(1 - (1 - confidence) / 2)
    sigma = np.sqrt(counts)
    lower_bound = np.maximum(counts - z * sigma, 0)
    upper_bound = counts + z * sigma
    return lower_bound, upper_bound

data_lower, data_upper = gaussian_confidence_interval(data_values)

# Plot Data Histogram with Confidence Levels
plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
plt.fill_between(data_edges[:-1], data_lower, data_upper, color='blue', alpha=0.2, label='95% CL')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('Data Histogram with Gaussian Confidence Levels')
plt.legend()
plt.grid(True)
plt.savefig('Plots/data_histogram_with_Gaussian_CL.png')
plt.close()

# Calculate ratio of data to MC
with np.errstate(divide='ignore', invalid='ignore'):
    ratio = np.divide(data_values, mc_values, out=np.zeros_like(data_values), where=mc_values != 0)
    ratio_error = np.sqrt(np.divide(data_values, mc_values**2, out=np.zeros_like(mc_values), where=mc_values != 0))

# Plot Ratio of Data to MC
plt.figure(figsize=(10, 7))
plt.errorbar(data_edges[:-1] + (data_edges[1] - data_edges[0]) / 2, ratio, yerr=ratio_error, fmt='o', color='black', label='Data/MC Ratio')
plt.axhline(y=1, color='gray', linestyle='--', label='Ratio = 1')
plt.fill_between(data_edges[:-1], 1 - ratio_error, 1 + ratio_error, color='green', alpha=0.3, label='±1σ')
plt.fill_between(data_edges[:-1], 1 - 2*ratio_error, 1 + 2*ratio_error, color='orange', alpha=0.2, label='±2σ')
plt.xlabel('X axis')
plt.ylabel('Data/MC Ratio')
plt.title('Ratio of Data to MC with ±1σ and ±2σ')
plt.legend()
plt.grid(True)
plt.show()
plt.close()
