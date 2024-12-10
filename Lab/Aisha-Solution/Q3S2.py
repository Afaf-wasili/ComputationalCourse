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

file_path = "histo.root"

# Open the ROOT file
file = uproot.open(file_path)

# Access histograms:
Data_hist = file["data"]
# Extract data:
Data_edges= Data_hist.axis().edges()
Data_Values= Data_hist.values()
#Plot histograms for Data:
plt.figure(figsize=(10, 7))
plt.step(Data_edges[:-1], Data_Values, color='blue', label='Data')  # Plot Data histogram
#Customization:
plt.title("DataHistogram")
plt.xlabel("Mase")
plt.ylabel("count")
plt.legend()
plt.grid()
plt.savefig("DataHistogram.png")
plt.show()
