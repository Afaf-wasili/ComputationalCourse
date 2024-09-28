import os
import uproot
import matplotlib.pyplot as plt
import numpy as np

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

# Calculate ratio
ratio = np.divide(data_values, mc_values)

# Plot histograms and ratio plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 14), sharex=True)
# Plot original histograms
ax1.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
ax1.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
ax1.set_ylabel('Counts')
ax1.set_title('Histograms ')
ax1.legend()
ax1.grid(True)

# Plot ratio plot
ax2.step(data_edges[:-1], ratio, where='mid', color='black', label='Data/MC Ratio')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Ratio')
ax2.axhline(1, color='gray', linestyle='--')  # Add a horizontal line at y=1 for reference
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
      #  plt.savefig("Plots/ratioMCData.png")
