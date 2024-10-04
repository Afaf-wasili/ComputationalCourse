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
ROOT.gStyle.SetMarkerSize(0.5)

# Set font for the legend
ROOT.gStyle.SetLegendFont(22)

# Open the ROOT file and get the trees
file = ROOT.TFile("mlpHiggs.root", "READ")
sig_tree = file.Get("sig_filtered")
bg_tree = file.Get("bg_filtered")

# Get total number of signal and background events
total_signal_events = sig_tree.GetEntries()
total_background_events = bg_tree.GetEntries()

# Initialize graphs for efficiency and purity
efficiency_graph = ROOT.TGraphErrors()
purity_graph = ROOT.TGraphErrors()

# Define the range of acolinearity thresholds to evaluate
acolin_thresholds = range(35, 180)  # Acolinearity thresholds from 35 to 179 degrees

# Loop over acolinearity thresholds
for acolin_threshold in acolin_thresholds:
    signal_entry_count = 0  # Count valid signal entries for each threshold
    background_entry_count = 0  # Count valid background entries for each threshold

    # Loop over signal entries
    for i in range(total_signal_events):
        sig_tree.GetEntry(i)
        # Count valid signal entries based on the acolinearity threshold
        if sig_tree.acolin >= acolin_threshold:
            signal_entry_count += 1

    # Loop over background entries
    for j in range(total_background_events):
        bg_tree.GetEntry(j)
        # Count valid background entries based on the acolinearity threshold
        if bg_tree.acolin >= acolin_threshold:
            background_entry_count += 1

    # Calculate efficiency
    efficiency = signal_entry_count / total_signal_events if total_signal_events > 0 else 0
    efficiency_error = (efficiency * (1 - efficiency) / total_signal_events) ** 0.5 if total_signal_events > 0 else 0

    # Calculate purity
    total_valid_events = signal_entry_count + background_entry_count
    purity = signal_entry_count / total_valid_events if total_valid_events > 0 else 0
    purity_error = (purity * (1 - purity) / total_valid_events) ** 0.5 if total_valid_events > 0 else 0

    # Set points in the graphs
    efficiency_graph.SetPoint(efficiency_graph.GetN(), acolin_threshold, efficiency)
    efficiency_graph.SetPointError(efficiency_graph.GetN() - 1, 0, efficiency_error)

    purity_graph.SetPoint(purity_graph.GetN(), acolin_threshold, purity)
    purity_graph.SetPointError(purity_graph.GetN() - 1, 0, purity_error)

# Configure graph appearance for efficiency
efficiency_graph.SetTitle("Signal Efficiency and Purity vs Acolinearity")
efficiency_graph.GetXaxis().SetTitle("Acolinearity (degrees)")
efficiency_graph.GetYaxis().SetTitle("Signal Efficiency / Purity")
efficiency_graph.SetLineColor(ROOT.kBlue)
efficiency_graph.SetMarkerStyle(20)
efficiency_graph.SetMarkerColor(ROOT.kBlue)

# Configure graph appearance for purity
purity_graph.SetLineColor(ROOT.kRed)
purity_graph.SetMarkerStyle(21)
purity_graph.SetMarkerColor(ROOT.kRed)

# Draw the graphs
canvas = ROOT.TCanvas("canvas", "Signal Efficiency and Purity vs Acolinearity", 800, 600)
canvas.SetGrid()  # Enable grid on the canvas
efficiency_graph.Draw("ALP")  # Draw efficiency graph
purity_graph.Draw("LP")  # Draw purity graph on the same canvas

# Set Y-axis range from 0.0 to 1.0
efficiency_graph.GetYaxis().SetRangeUser(0.009, 1.01)

# Create and configure the legend
legend = ROOT.TLegend(0.17, 0.17, 0.3, 0.34)  # Define legend position
legend.SetHeader("g + g \\rightarrow c + \\bar{c}")  # Add a header to the legend
legend.AddEntry(efficiency_graph, "Efficiency", "lp")  # Add efficiency entry
legend.AddEntry(purity_graph, "Purity", "lp")  # Add purity entry
legend.Draw()  # Draw the legend

canvas.Update()
ROOT.gApplication.Run()

# Close the file
file.Close()
