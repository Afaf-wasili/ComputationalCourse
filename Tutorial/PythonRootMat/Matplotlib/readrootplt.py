import os
import uproot
import matplotlib.pyplot as plt

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
    '''
    # Print extracted data
    print("Data Histogram:")
    print("Edges:", data_edges)
    print("Values:", data_values)

    print("MC Histogram:")
    print("Edges:", mc_edges)
    print("Values:", mc_values)
    
    # Plot histograms
    plt.figure(figsize=(10, 7))
    plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
    plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
    plt.xlabel('X axis')
    plt.ylabel('Counts')
    plt.title('Histograms from ROOT File')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("Plots/DataMC.png")
    '''
    # Plot Data Histogram
    plt.figure(figsize=(10, 7))
    plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')
    plt.xlabel('X axis')
    plt.ylabel('Counts')
    plt.title('Data Histogram')
    plt.legend()
    plt.grid(True)
#    plt.show()
    plt.savefig("Plots/Data.png")

    # Plot MC Histogram
    plt.figure(figsize=(10, 7))
    plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')
    plt.xlabel('X axis')
    plt.ylabel('Counts')
    plt.title('MC Histogram')
    plt.legend()
    plt.grid(True)
 #   plt.show()
    plt.savefig("Plots/MC.png")
