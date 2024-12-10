import uproot
import numpy as np
import matplotlib.pyplot as plt

# Questions :
# 1. Access and define the Histogram: 
# 2. Extract Data:
# 3. Customization:
#    - Do the labels, title, and grid add to the visualization.
# 4. Save the Plot:
#    - Modify the script to save the "Data Histogram" plot as a PNG file named "DataHistogram.png".

file_path = "Plots/histo.root"

# Open the ROOT file
file = uproot.open(file_path)

# Access histograms:

# Extract data:

#Plot histograms for Data:
plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, color='blue', label='Data')  # Plot Data histogram
#Customization:
