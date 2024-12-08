import ROOT
import numpy as np

# File path and reading ROOT file
file_path = "../../../mlpHiggs.root"
file = ROOT.TFile(file_path, "READ")
bg_tree = file.Get("bg_filtered")

# Create and fill the histogram for ptsumf
bg_hist = ROOT.TH1F("bg_ptsumf", "ptsumf - Background", 150, 0, 0.5)
for j in range(bg_tree.GetEntries()):
    bg_tree.GetEntry(j)
    bg_hist.Fill(bg_tree.ptsumf)

bg_hist.SetStats(0)  # Disable stats box for cleaner plot

# Create the canvas
canvas = ROOT.TCanvas("canvas", "ptsumf with Confidence Level", 800, 600)
bg_hist.GetXaxis().SetTitle("ptsumf")
bg_hist.GetYaxis().SetTitle("Events")
bg_hist.GetXaxis().SetRangeUser(0, 0.6)
bg_hist.GetYaxis().SetRangeUser(0, 50)

# Draw the histogram
bg_hist.SetLineColor(ROOT.kBlack)
bg_hist.SetLineWidth(2)
bg_hist.Draw("HIST")

# Calculate confidence level and prepare for plotting confidence intervals
mean = bg_hist.GetMean()
sigma = bg_hist.GetStdDev()
confidence_level = 2
n_bins = bg_hist.GetNbinsX()

# Arrays to store points for the filled area
x_values_conf = []
y_values_upper = []
y_values_lower = []

for i in range(1, n_bins + 1):
    x = bg_hist.GetBinCenter(i)
    y = bg_hist.GetBinContent(i)
    
    if y > 0:
        x_values_conf.append(x)
        y_values_upper.append(y + confidence_level)
        y_values_lower.append(y - confidence_level)

# Create a filled graph for the confidence intervals
n_points = len(x_values_conf)
if n_points > 0:
    fill_graph = ROOT.TGraph(2 * n_points)
    for i in range(n_points):
        fill_graph.SetPoint(i, x_values_conf[i], y_values_upper[i])
        fill_graph.SetPoint(n_points + i, x_values_conf[n_points - 1 - i], y_values_lower[n_points - 1 - i])
    fill_graph.SetFillColor(ROOT.kBlue - 7)
    fill_graph.SetFillStyle(3001)
    fill_graph.Draw("F SAME")

# Create and style the legend
legend = ROOT.TLegend(0.7, 0.75, 0.9, 0.85)  # Smaller legend box
legend.SetTextSize(0.03)
legend.SetFillColor(0)  # Transparent background
legend.SetLineColor(0)  # No border for the legend
legend.AddEntry(bg_hist, "ptsumf", "l")
if n_points > 0:
    legend.AddEntry(fill_graph, "Confidence Level", "f")
legend.Draw()

# Save the canvas as a PNG file
canvas.SaveAs("ptsumfCL.png")

# Close the ROOT file
file.Close()
