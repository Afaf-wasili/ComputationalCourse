import ROOT
'''
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
'''
# Open the ROOT file and get the signal tree
file = ROOT.TFile("mlpHiggs.root", "READ")
sig_tree = file.Get("sig_filtered")

# Get total number of signal events
total_signal_events = sig_tree.GetEntries()

# Initialize graph for efficiency
efficiency_graph = ROOT.TGraphErrors()

# Define the range of acolinearity thresholds to evaluate/
acolin_thresholds = range(80, 200)  # Acolinearity thresholds from 35 to 180 degrees

# Loop over acolinearity thresholds
for i in acolin_thresholds:
    signal_entry_count = 0  # Count valid signal entries for each threshold

    # Loop over signal entries
    for j in range(total_signal_events):
        sig_tree.GetEntry(j)
        # Count valid signal entries based on the acolinearity threshold
        if sig_tree.acolin >= i:    
           
           signal_entry_count += 1

    # Calculate efficiency
    efficiency = signal_entry_count / total_signal_events 
    efficiency_error = (efficiency * (1 - efficiency) / total_signal_events) ** 0.5 

    # Set points in the efficiency graph
    efficiency_graph.SetPoint(efficiency_graph.GetN(), i, efficiency)
    efficiency_graph.SetPointError(efficiency_graph.GetN() - 1, 0, efficiency_error)

# Configure graph appearance for efficiency
efficiency_graph.SetTitle("Signal Efficiency vs Acolinearity")
efficiency_graph.GetXaxis().SetTitle("Acolinearity (degrees)")
efficiency_graph.GetYaxis().SetTitle("Signal Efficiency")
efficiency_graph.SetLineColor(ROOT.kBlue)
efficiency_graph.SetMarkerStyle(20)
efficiency_graph.SetMarkerColor(ROOT.kBlue)

# Draw the efficiency graph
canvas = ROOT.TCanvas("canvas", "Signal Efficiency vs Acolinearity", 800, 600)
canvas.SetGrid()  # Enable grid on the canvas
efficiency_graph.Draw("ALP")  # Draw efficiency graph

# Set Y-axis range from 0.0 to 1.0
#efficiency_graph.GetYaxis().SetRangeUser(0.0, 1.0)

canvas.Update()
ROOT.gApplication.Run()

# Close the file
file.Close()

