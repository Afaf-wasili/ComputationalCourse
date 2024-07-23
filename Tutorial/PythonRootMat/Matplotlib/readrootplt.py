import uproot
import numpy as np
import matplotlib.pyplot as plt

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

# Plot histograms
plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('Histograms from ROOT File')
plt.legend()
plt.grid(True)
plt.savefig("Plots/DataMC.png")
plt.show()

# Save individual plots for Data and MC
plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('Data Histogram')
plt.legend()
plt.grid(True)
plt.savefig("Plots/Data.png")
plt.show()

plt.figure(figsize=(10, 7))
plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('MC Histogram')
plt.legend()
plt.grid(True)
plt.savefig("Plots/MC.png")
plt.show()
