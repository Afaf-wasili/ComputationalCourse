import ROOT

# Apply the modern style
ROOT.gROOT.SetStyle("ATLAS")  # Use "ATLAS" for the modern style
ROOT.gROOT.ForceStyle()
ROOT.gStyle.SetPalette(ROOT.kRainbow)  # Set the color palette to Rainbow

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
ROOT.gStyle.SetLabelSize(0.03, "Z")
ROOT.gStyle.SetMarkerSize(0.5)

# Set label offset for axes
ROOT.gStyle.SetLabelOffset(0.005, "X")  # Offset for x-axis labels
ROOT.gStyle.SetLabelOffset(0.005, "Y")  # Offset for y-axis labels
ROOT.gStyle.SetLabelOffset(0.005, "Z")  # Offset for z-axis labels

# Open the ROOT file and retrieve histograms
file = ROOT.TFile.Open("mlpHiggs.root")

# Retrieve signal and background trees
sig_tree = file.Get("sig_filtered")
bg_tree = file.Get("bg_filtered")

# Create a 2D histogram using binning for background vs signal
nbins_x = 100  # Set number of bins for x-axis (Background)
nbins_y = 100  # Set number of bins for y-axis (Signal)
x_min = 0      # Set minimum value for x-axis (change as needed)
x_max = 180    # Set maximum value for x-axis (change as needed)
y_min = 0      # Set minimum value for y-axis (change as needed)
y_max = 180    # Set maximum value for y-axis (change as needed)

# Create a 2D histogram
hist_2d = ROOT.TH2F("hist_2d", "Background vs Signal;Background;Signal",
                     nbins_x, x_min, x_max,
                     nbins_y, y_min, y_max)

# Loop over background entries and fill the 2D histogram
for j in range(bg_tree.GetEntries()):
    bg_tree.GetEntry(j)
    # Fill with the background variable on the x-axis and some variable from signal tree
    for i in range(sig_tree.GetEntries()):
        sig_tree.GetEntry(i)
        # Fill the histogram using the chosen variables from both trees
        hist_2d.Fill(bg_tree.acolin, sig_tree.acolin)  # Replace acolin with actual variable names

# Set z-axis label options
hist_2d.GetZaxis().SetLabelSize(0.005)  # Set the size of z-axis labels
hist_2d.GetZaxis().SetTitle("Counts")  # Optional: Set the title for the z-axis

# Set z-axis range
hist_2d.GetZaxis().SetRangeUser(0, hist_2d.GetMaximum())  # Show all counts

# Draw the 2D histogram
c = ROOT.TCanvas("c", "Background vs Signal", 1000, 800)  # Increase the canvas size
hist_2d.Draw("COLZ")  # Use "COLZ" to draw with color

# Show the canvas
c.Show()
c.SaveAs("test.png")

# Close the ROOT file
file.Close()
