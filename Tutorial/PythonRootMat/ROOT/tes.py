import ROOT
import numpy as np

# Define the path to the ROOT file
file_path = "histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms
data_hist = file.Get("data")
mc_hist = file.Get("MC")

# Normalize histograms if needed
data_hist.Scale(1 / data_hist.Integral())
mc_hist.Scale(1 / mc_hist.Integral())

# Create a ratio histogram
ratio_hist = data_hist.Clone("ratio_hist")
ratio_hist.Divide(mc_hist)

# Create a canvas for drawing
canvas = ROOT.TCanvas("canvas", "Data/MC Ratio", 800, 600)

# Draw the ratio histogram with larger markers
ratio_hist.SetMarkerStyle(20)
ratio_hist.SetMarkerSize(1.2)  # Increase marker size for clarity
ratio_hist.SetMarkerColor(ROOT.kBlue)
ratio_hist.SetLineColor(ROOT.kBlue)
ratio_hist.Draw("E")

# Calculate the upper and lower confidence levels
n_bins = ratio_hist.GetNbinsX()
x_values = []
y_values_upper = []
y_values_lower = []

for i in range(1, n_bins + 1):
    data_value = data_hist.GetBinContent(i)
    mc_value = mc_hist.GetBinContent(i)

    if mc_value > 0:  # Avoid division by zero
        ratio_value = data_value / mc_value
        # Calculate the statistical uncertainty
        data_error = np.sqrt(data_value)  # Poisson error for data
        mc_error = mc_value * np.sqrt(1. / mc_value)  # Poisson error for MC

        # Calculate upper and lower confidence limits
        upper_bound = ratio_value + 1.96 * np.sqrt((data_error / mc_value) ** 2 + (data_value * mc_error / mc_value ** 2) ** 2)
        lower_bound = ratio_value - 1.96 * np.sqrt((data_error / mc_value) ** 2 + (data_value * mc_error / mc_value ** 2) ** 2)

        x_values.append(ratio_hist.GetBinCenter(i))
        y_values_upper.append(upper_bound)
        y_values_lower.append(lower_bound)

# Create a filled area for the confidence level
fill_graph = ROOT.TGraph(2 * len(x_values))

# Set points for the upper and lower limits
for i in range(len(x_values)):
    fill_graph.SetPoint(i, x_values[i], y_values_upper[i])  # Upper points
    fill_graph.SetPoint(len(x_values) + i, x_values[len(x_values) - 1 - i], y_values_lower[len(x_values) - 1 - i])  # Lower points (reverse order)

fill_graph.SetFillColor(ROOT.kYellow)
fill_graph.SetFillStyle(3001)  # Solid filling style

# Draw the filled area first
fill_graph.Draw("F SAME")

# Draw the ratio line again to ensure it's on top of the filled area
ratio_hist.Draw("E SAME")

# Add legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(ratio_hist, "Data / MC Ratio", "lep")
legend.AddEntry(fill_graph, "Confidence Level Area", "f")
legend.Draw()

# Set y-axis limits to be close to the ratio
y_min = min(y_values_lower) if y_values_lower else 0
y_max = max(y_values_upper) if y_values_upper else 1.5  # Set a reasonable upper limit

canvas.SetLogy()  # Set logarithmic scale if needed, comment this line if not
canvas.Update()
canvas.Draw()

# Adjust the y-axis limits based on the ratio histogram
ratio_hist.GetYaxis().SetRangeUser(y_min * 0.5, y_max * 1.5)

# Draw the canvas
canvas.Update()
canvas.Draw()

# Save the canvas in the Plots directory
canvas.SaveAs("Plots/ratio_plot_CL.png")

# Close the ROOT file
file.Close()
