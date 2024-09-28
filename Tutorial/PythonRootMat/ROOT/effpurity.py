import ROOT
import numpy as np

# Define the absolute path to the ROOT file
file_path = "../Matplotlib/Plots/histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms
signal_hist = file.Get("data")  # Signal
background_hist = file.Get("MC")  # Background

# Create new histograms for efficiency, purity, and their product
efficiency_hist = signal_hist.Clone("efficiency")
purity_hist = signal_hist.Clone("purity")
product_hist = signal_hist.Clone("product")

# Create arrays for errors
efficiency_errors = np.zeros(signal_hist.GetNbinsX())
purity_errors = np.zeros(signal_hist.GetNbinsX())
product_errors = np.zeros(signal_hist.GetNbinsX())

# Calculate efficiency, purity, and their errors
for bin in range(1, signal_hist.GetNbinsX() + 1):
    signal_count = signal_hist.GetBinContent(bin)
    background_count = background_hist.GetBinContent(bin)
    
    # Efficiency calculation
    total_mc_count = background_count
    if total_mc_count > 0:
        efficiency = signal_count / total_mc_count
        efficiency_errors[bin - 1] = efficiency * np.sqrt(1 / signal_count + 1 / total_mc_count) if signal_count > 0 else 0
    else:
        efficiency = 0
        efficiency_errors[bin - 1] = 0
    efficiency_hist.SetBinContent(bin, efficiency)

    # Purity calculation
    total_count = signal_count + background_count
    if total_count > 0:
        purity = signal_count / total_count
        purity_errors[bin - 1] = purity * np.sqrt(1 / signal_count + 1 / total_count) if signal_count > 0 else 0
    else:
        purity = 0
        purity_errors[bin - 1] = 0
    purity_hist.SetBinContent(bin, purity)

    # Product calculation
    product = efficiency * purity
    product_hist.SetBinContent(bin, product)
    product_errors[bin - 1] = product * np.sqrt((efficiency_errors[bin - 1] / efficiency) ** 2 + (purity_errors[bin - 1] / purity) ** 2) if efficiency > 0 and purity > 0 else 0

# Set up the canvas for drawing
canvas = ROOT.TCanvas("canvas", "Efficiency, Purity and Product", 800, 600)

# Draw efficiency histogram with error bars
efficiency_hist.SetTitle("Efficiency, Purity and Product")
efficiency_hist.SetLineColor(ROOT.kGreen)
efficiency_hist.SetMarkerColor(ROOT.kGreen)
efficiency_hist.Draw("HIST E")

# Draw purity histogram with error bars
purity_hist.SetLineColor(ROOT.kMagenta)
purity_hist.SetMarkerColor(ROOT.kMagenta)
purity_hist.Draw("HIST E SAME")

# Draw product histogram with error bars
product_hist.SetLineColor(ROOT.kCyan)
product_hist.SetMarkerColor(ROOT.kCyan)
product_hist.Draw("HIST E SAME")

# Set axis titles
efficiency_hist.GetYaxis().SetTitle("Values")
efficiency_hist.GetXaxis().SetTitle("Bins")

# Create and draw the legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(efficiency_hist, "Efficiency", "l")
legend.AddEntry(purity_hist, "Purity", "l")
legend.AddEntry(product_hist, "Efficiency * Purity", "l")
legend.Draw()

# Save the canvas as an image
canvas.SaveAs("Plots/Efficiency_Purity_Product.png")

# Close the ROOT file
file.Close()
