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

# Retrieve the data histogram
data_hist = file.Get("data")

# Set up the canvas for drawing
canvas = ROOT.TCanvas("canvas", "Data Histogram with Gaussian Fit", 800, 600)
canvas.SetMargin(0.15, 0.05, 0.15, 0.1)

# Set colors and remove statistics box
data_hist.SetLineColor(ROOT.kBlue)
data_hist.SetStats(0)

# Draw the histogram
data_hist.Draw("HIST")
data_hist.GetXaxis().SetTitle("Mass")
data_hist.GetYaxis().SetTitle("Counts")
#data_hist.GetXaxis().SetRangeUser(70, 120)

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
#print("sigma=",sigma ,"+/-", sigma_error )

# Create a legend to show fit parameters and errors
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(data_hist, "Data", "l")
legend.AddEntry(gauss, "Gaussian Fit", "l")
legend.AddEntry("", f"#mu: {mean:.2f} #pm {mean_error:.3f}", "")
legend.AddEntry("", f"#sigma: {sigma:.2f} #pm {sigma_error:.3f}", "")
legend.Draw()

# Save the canvas as an image
canvas.SaveAs("Plots/Data_Histogram_with_Gaussian_Fit_and_Errors.png")
#gauss.SaveAs("Plots/Data_Histogram_with_Gaussian_Fit_and_Errors.root")
# Close the ROOT file
file.Close()

