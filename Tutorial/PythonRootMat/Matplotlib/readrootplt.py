import uproot
import numpy as np
import matplotlib.pyplot as plt

file_path = "Plots/histo.root"

# Open the root file
file = uproot.open(file_path)

# Access histograms
data_hist = file["data"]
#mc_hist = file["MC"]

# Extract data
data_edges = data_hist.axis().edges()  #refers to the boundaries or limits of the bins 
data_values = data_hist.values()   #refers to the count or frequency of data points that fall into each bin of the histogram. It represents how many data points are in each interval defined by the edges

#mc_edges = mc_hist.axis().edges()
#mc_values = mc_hist.values()
'''
# Plot histograms for MC and data
plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data') #[:-1] is used to exclude the last element of the array, which is helpful in ensuring that the number of x-coordinates matches the number of y-values in step plots.
plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('Histograms from ROOT File')
plt.legend()
plt.grid(True)
plt.savefig("Plots/DataMC.png")
plt.show()
'''
# Save individual plots for Data and MC
#plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, color='blue', label='Data')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('Data Histogram')
plt.legend()
plt.grid(True)
#plt.savefig("Plots/Data.png")
plt.show()
'''
plt.figure(figsize=(10, 7))
plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('MC Histogram')
plt.legend()
plt.grid(True)
plt.savefig("Plots/MC.png")
plt.show()
'''
