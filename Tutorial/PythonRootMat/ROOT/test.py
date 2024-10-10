import ROOT

# Apply the modern style
ROOT.gROOT.SetStyle("ATLAS")
ROOT.gROOT.ForceStyle()

# Set font for axis titles and labels
ROOT.gStyle.SetLabelFont(22, "X")
ROOT.gStyle.SetLabelFont(22, "Y")
ROOT.gStyle.SetTitleFont(22, "X")
ROOT.gStyle.SetTitleFont(22, "Y")

# Set size of axis titles and labels
ROOT.gStyle.SetLabelSize(0.03, "X")
ROOT.gStyle.SetLabelSize(0.03, "Y")
ROOT.gStyle.SetTitleSize(0.04, "X")
ROOT.gStyle.SetTitleSize(0.04, "Y")

# Set font for the legend
ROOT.gStyle.SetLegendFont(22)

# Define the absolute path to the ROOT file
file_path = "histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the data and MC histograms
data_hist = file.Get("data")
mc_hist = file.Get("MC")  # Make sure you have the MC histogram loaded

# Set up the canvas with two pads
canvas = ROOT.TCanvas("canvas", "Data Histogram with Gaussian Fit and Ratio Plot", 800, 600)
canvas.Divide(1, 2)

# ---- Pad 1: Data Histogram with Gaussian Fit ----
canvas.cd(1)
canvas.SetMargin(0.15, 0.05, 0.15, 0.1)

# Set colors and remove statistics box
data_hist.SetLineColor(ROOT.kBlue)
data_hist.SetStats(0)

# Draw the histogram
data_hist.Draw("HIST")
data_hist.GetXaxis().SetTitle("Mass")
data_hist.GetYaxis().SetTitle("Counts")

# Create and set up the Gaussian function
gauss = ROOT.TF1("gauss", "gaus", 70, 120)
gauss.SetParLimits(0, 220, 300)  # Set limits for amplitude

# Fit the Gaussian to the data histogram
data_hist.Fit(gauss, "")
gauss.SetLineColor(ROOT.kRed)
gauss.Draw("SAME")

# Get fit parameters and their errors
mean = gauss.GetParameter(1)
sigma = gauss.GetParameter(2)
mean_error = gauss.GetParError(1)
sigma_error = gauss.GetParError(2)

# Create a legend to show fit parameters and errors
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(data_hist, "Data", "l")
legend.AddEntry(gauss, "Gaussian Fit", "l")
legend.AddEntry("", f"#mu: {mean:.2f} #pm {mean_error:.3f}", "")
legend.AddEntry("", f"#sigma: {sigma:.2f} #pm {sigma_error:.3f}", "")
legend.Draw()

# ---- Pad 2: Ratio Plot ----
canvas.cd(2)
canvas.SetMargin(0.15, 0.05, 0.15, 0.1)

# Calculate the ratio histogram
ratio_hist = data_hist.Clone("ratio_hist")
ratio_hist.Divide(mc_hist)

# Clone the MC histogram for the error calculation
h_mc_error = mc_hist.Clone("h_mc_error")
h_mc_error.Divide(mc_hist)  # This step might depend on your error calculations

# Set styles for the ratio histogram
ratio_hist.SetLineColor(ROOT.kBlack)
ratio_hist.SetMarkerStyle(20)
ratio_hist.SetMarkerSize(0.3)
ratio_hist.SetMarkerColor(ROOT.kBlack)

# Draw the ratio histogram
ratio_hist.Draw("E")  # Draw with error bars

# Set titles for the ratio plot
ratio_hist.GetYaxis().SetTitle("Data/MC Ratio")
ratio_hist.GetYaxis().SetTitleSize(0.1)
ratio_hist.GetYaxis().SetLabelSize(0.08)
ratio_hist.GetYaxis().SetTitleOffset(0.4)

# Set x-axis labels and title for the bottom pad
ratio_hist.GetXaxis().SetTitle("Mass")
ratio_hist.GetXaxis().SetLabelSize(0.0812)
ratio_hist.GetXaxis().SetTitleSize(0.12)
ratio_hist.GetXaxis().SetTitleOffset(1.2)

# Increase font size for axis labels in the ratio plot
ratio_hist.GetYaxis().SetNdivisions(505)

# Save the canvas as an image
canvas.SaveAs("Plots/Data_MC_Ratio_Histograms.png")

# Close the ROOT file
file.Close()
