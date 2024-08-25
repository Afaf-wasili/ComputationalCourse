'''
import numpy as np
import matplotlib.pyplot as plt

# Generate example x-values (similar to m_H in the provided image)
x_values = np.linspace(110, 500, 100)

# Generate random CL data for the example
np.random.seed(0)
cl_data = np.random.normal(loc=1, scale=0.2, size=(1000, len(x_values)))

# Calculate mean and standard deviations for the CL data
mean_cl = np.mean(cl_data, axis=0)
std_cl = np.std(cl_data, axis=0)

# Calculate ±1σ and ±2σ intervals
one_sigma_lower = mean_cl - std_cl
one_sigma_upper = mean_cl + std_cl
two_sigma_lower = mean_cl - 2 * std_cl
two_sigma_upper = mean_cl + 2 * std_cl

# Plotting
plt.figure(figsize=(10, 6))

# Plot the mean CL
plt.plot(x_values, mean_cl, color='black', linestyle='-', label='Observed')

#Observed": The actual data observed from your histogram.
"Bkg. Expected": Theoretical or model-based expectation of the background level, which serves as a reference point in your analysis.

# Plot the expected CL
expected_cl = mean_cl * 0.95
plt.plot(x_values, expected_cl, color='black', linestyle='--', label='Bkg. Expected')

# Fill between for ±1σ and ±2σ intervals
plt.fill_between(x_values, one_sigma_lower, one_sigma_upper, color='green', alpha=0.3, label='±1σ')
plt.fill_between(x_values, two_sigma_lower, two_sigma_upper, color='yellow', alpha=0.2, label='±2σ')

# Add labels and legend
plt.xlabel(r'$m_H$ [GeV]')
plt.ylabel(r'95% CL Limit on $\mu$')
plt.yscale('log')
plt.title('Confidence Limits with Mean Signal')
plt.legend()

# Display plot
plt.grid(True)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
import uproot

# Define the file path and open the ROOT file
file_path = "Plots/histo.root"
file = uproot.open(file_path)

# Access the "data" histogram
data_hist = file["data"]

# Extract data
data_edges = data_hist.axis().edges()
data_values = data_hist.values()
data_centers = (data_edges[:-1] + data_edges[1:]) / 2

# Calculate mean and standard deviation for the histogram data
mean_cl = np.mean(data_values)
std_cl = np.std(data_values)

# Calculate ±1σ and ±2σ intervals
one_sigma_lower = mean_cl - std_cl
one_sigma_upper = mean_cl + std_cl
two_sigma_lower = mean_cl - 2 * std_cl
two_sigma_upper = mean_cl + 2 * std_cl

# Plotting
plt.figure(figsize=(10, 6))

# Plot the mean CL
plt.plot(data_centers, np.full_like(data_centers, mean_cl), color='black', linestyle='-', label='Observed')

# Plot the expected CL
expected_cl = mean_cl * 0.95
plt.plot(data_centers, np.full_like(data_centers, expected_cl), color='black', linestyle='--', label='Bkg. Expected')

# Fill between for ±1σ and ±2σ intervals
plt.fill_between(data_centers, one_sigma_lower, one_sigma_upper, color='green', alpha=0.3, label='±1σ')
plt.fill_between(data_centers, two_sigma_lower, two_sigma_upper, color='yellow', alpha=0.2, label='±2σ')

# Add labels and legend
plt.xlabel(r'$m_H$ [GeV]')
plt.ylabel(r'95% CL Limit on $\mu$')
plt.yscale('log')
plt.title('Confidence Limits with Mean Signal')
plt.legend()

# Display plot
plt.grid(True)
plt.tight_layout()
plt.show()
