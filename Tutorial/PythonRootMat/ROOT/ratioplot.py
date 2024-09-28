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

# Define the path to the ROOT file
file_path = "../Matplotlib/Plots/histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms
data_hist = file.Get("data")
mc_hist = file.Get("MC")
data_hist.SetLineColor(ROOT.kBlue)
mc_hist.SetLineColor(ROOT.kGreen)

# Set up the canvas for drawing with two pads
canvas = ROOT.TCanvas("canvas", "", 800, 800)

# Create two pads: one for the histograms and one for the ratio
pad1 = ROOT.TPad("pad1", "Data and MC", 0.0, 0.32, 1.0, 1.0)  # Adjusted lower boundary (was 0.3)
pad2 = ROOT.TPad("pad2", "Ratio", 0, 0.05, 1, 0.32)  # Adjusted upper boundary (was 0.02)
# Set margins for the pads
pad1.SetBottomMargin(0.02)  # Add a small bottom margin to prevent overlap
pad2.SetTopMargin(0.02)     # Add a small top margin for better separation
pad2.SetBottomMargin(0.3)   # Set margin for the bottom pad for labels
pad1.Draw()
pad2.Draw()

# Draw histograms in the top pad
pad1.cd()
data_hist.Draw("HIST")
mc_hist.Draw("HIST SAME")

# Remove x-axis from the top pad (shared x-axis will be on the bottom pad)
data_hist.GetXaxis().SetLabelSize(0)
data_hist.GetXaxis().SetTitleSize(0)

# Create and draw the legend in the first pad
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)  # Define legend position (x1, y1, x2, y2)
legend.AddEntry(data_hist, "Data", "l")    # Add data histogram to legend
legend.AddEntry(mc_hist, "MC", "l")        # Add MC histogram to legend
legend.Draw()

# Create the ratio plot in the second pad
pad2.cd()

# Calculate the ratio histogram manually
ratio_hist = data_hist.Clone("ratio_hist")
ratio_hist.Divide(mc_hist)

# Set the styles for the ratio histogram
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

# Set titles for the data histogram (top pad)
data_hist.GetYaxis().SetTitle("Counts")

# Save the canvas as an image
canvas.SaveAs("Plots/Data_MC_Ratio_Histograms_Adjusted.png")

# Close the ROOT file
file.Close()
