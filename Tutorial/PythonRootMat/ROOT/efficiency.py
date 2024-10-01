import ROOT
import numpy as np

# Define the absolute path to the ROOT file
file_path = "sorted_mass.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms for protons and kaons
signal_hist = file.Get("histProton")  # Signal histogram
background_hist = file.Get("histKaon")  # Background histogram

# Create a new histogram for efficiency
efficiency_hist = signal_hist.Clone("efficiency")

# Calculate efficiency and its errors
for bin in range(1, signal_hist.GetNbinsX() + 1):
    signal_count = signal_hist.GetBinContent(bin)
    background_count = background_hist.GetBinContent(bin)

    total_count = signal_count + background_count  # Total count includes both signal and background

    if total_count > 0:
        # Efficiency calculation
        efficiency = signal_count / total_count
        efficiency_hist.SetBinContent(bin, efficiency)

        # Error calculation using error propagation formula
        error = efficiency * np.sqrt((1 / signal_count if signal_count > 0 else 0) + 
                                      (1 / background_count if background_count > 0 else 0))
        efficiency_hist.SetBinError(bin, error)
    else:
        efficiency_hist.SetBinContent(bin, 0)
        efficiency_hist.SetBinError(bin, 0)

# Set up the canvas for drawing
canvas = ROOT.TCanvas("canvas", "Efficiency", 800, 600)

# Draw efficiency histogram with error bars
efficiency_hist.SetTitle("Efficiency; Bins; Efficiency")
efficiency_hist.SetLineColor(ROOT.kGreen)
efficiency_hist.SetMarkerColor(ROOT.kGreen)
efficiency_hist.Draw("HIST E")

# Save the canvas as an image
canvas.SaveAs("Plots/Efficiency.png")

# Close the ROOT file
file.Close()
