import ROOT

# Open the ROOT file
file_path = "../Matplotlib/Plots/histo.root"  # Update this path as necessary
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms
data_hist = file.Get("data")
mc_hist = file.Get("MC")

# Create a 2D histogram
nbins_x = 100  # Number of bins in the x direction
nbins_y = 100  # Number of bins in the y direction
hist_2d = ROOT.TH2F("hist_2d", "Data vs MC;Data;MC;Counts", nbins_x, 60, 130, nbins_y, 60, 130)

# Fill the 2D histogram using data and mc histograms
for i in range(1, data_hist.GetNbinsX() + 1):  # Loop over bins of data_hist
    data_value = data_hist.GetBinContent(i)  # Get content from data_hist
    data_bin_center = data_hist.GetBinCenter(i)  # Get center of the bin
    
    # Fill the 2D histogram for each entry in data_hist
    for _ in range(int(data_value)):  # Repeat filling based on the number of entries in data_hist
        # Loop through the bins in mc_hist to find corresponding values
        for j in range(1, mc_hist.GetNbinsX() + 1):
            mc_value = mc_hist.GetBinContent(j)  # Get content from mc_hist
            mc_bin_center = mc_hist.GetBinCenter(j)  # Get center of the bin

            # Fill the 2D histogram using the data bin center and corresponding mc bin center
            hist_2d.Fill(data_bin_center, mc_bin_center)

# Set up the canvas for drawing
canvas = ROOT.TCanvas("canvas", "Data vs MC 2D Histogram", 800, 600)

# Draw the 2D histogram
hist_2d.Draw("COLZ")  # Draw the histogram with color

# Update and save the canvas as an image
canvas.Update()  # Ensure canvas is refreshed
canvas.SaveAs("Plots/Data_MC_2D_Histogram.png")

# Close the ROOT file
file.Close()
