import os
import uproot
import matplotlib.pyplot as plt

# Specify the path to the ROOT file
file_path = "CMS/histo.root"

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"The file {file_path} does not exist. Please check the path.")
else:
    try:
        # Open the ROOT file
        with uproot.open(file_path) as file:
            # Access the histograms
            data_hist = file["data"]
            mc_hist = file["MC"]

            # Check if histograms were successfully accessed
            if data_hist is None:
                print("Histogram 'data' not found in the file.")
            if mc_hist is None:
                print("Histogram 'MC' not found in the file.")
            
            # Extract data from histograms
            # Call methods correctly
            data_axis = data_hist.axis()
            data_edges = data_axis.edges()  # Call method with parentheses
            data_values = data_hist.values()

            mc_axis = mc_hist.axis()
            mc_edges = mc_axis.edges()  # Call method with parentheses
            mc_values = mc_hist.values()

            # Print the extracted data to check
            print("Data Histogram:")
            print("Edges:", data_edges)
            print("Values:", data_values)

            print("MC Histogram:")
            print("Edges:", mc_edges)
            print("Values:", mc_values)

        # Plot histograms using Matplotlib
        plt.figure(figsize=(10, 7))

        # Plot the data histogram
        plt.step(data_edges[:-1], data_values, where='mid', color='blue', label='Data')

        # Plot the MC histogram
        plt.step(mc_edges[:-1], mc_values, where='mid', color='red', label='MC')

        # Add labels, title, and legend
        plt.xlabel('X axis')
        plt.ylabel('Counts')
        plt.title('Histograms from ROOT File')
        plt.legend()
        plt.grid(True)

        # Show plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
