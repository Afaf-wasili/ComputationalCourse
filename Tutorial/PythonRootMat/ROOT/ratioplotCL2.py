import ROOT
import numpy as np

# Define the path to the ROOT file
file_path = "../Matplotlib/Plots/histo.root"

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

# Draw ratio with larger markers
ratio_hist.SetMarkerStyle(20)
ratio_hist.SetMarkerSize(1.2)  # Increase marker size for clarity
ratio_hist.SetMarkerColor(ROOT.kBlue)
ratio_hist.SetLineColor(ROOT.kBlue)  # Set line color for the ratio
ratio_hist.Draw("E")

# Calculate the mean and standard deviation for confidence level calculation
mean_ratio = ratio_hist.GetMean()
stddev_ratio = ratio_hist.GetStdDev()
n_bins = ratio_hist.GetNbinsX()

# Define the 95% confidence level area
confidence_level = 1.96 * (stddev_ratio / np.sqrt(n_bins))  # 95% CL margin

# Prepare TGraph for filling the confidence level
x_values = []
y_values_upper = []
y_values_lower = []
n_points = 0  # To keep track of valid points

for i in range(1, n_bins + 1):
    x = ratio_hist.GetBinCenter(i)
    y = ratio_hist.GetBinContent(i)
    if y > 0:  # Only add points if the ratio is greater than zero
        x_values.append(x)
        y_values_upper.append(y + confidence_level)  # Upper limit
        y_values_lower.append(y - confidence_level)  # Lower limit
        n_points += 1  # Count valid points

# Create a filled area only if there are valid points
if n_points > 0:
    fill_graph = ROOT.TGraph(2 * n_points)

    for i in range(n_points):
        fill_graph.SetPoint(i, x_values[i], y_values_upper[i])  # Upper points
        fill_graph.SetPoint(n_points + i, x_values[n_points - 1 - i], y_values_lower[n_points - 1 - i])  # Lower points (reverse order)

    fill_graph.SetFillColor(ROOT.kYellow + 2)  # Light gray color
    fill_graph.SetFillStyle(3001)  # Solid filling style
    fill_graph.Draw("F")  # Draw filled area first

# Draw the ratio line
ratio_hist.Draw("E SAME")

# Add legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(ratio_hist, "Data / MC Ratio", "lep")
if n_points > 0:
    legend.AddEntry(fill_graph, "Confidence Level", "f")
legend.Draw()

# Draw the canvas
canvas.Update()
canvas.Draw()

# Save the canvas in the Plots directory
canvas.SaveAs("Plots/ratio_plot_CL.png")
