import ROOT as rt

# Set canvas dimensions
W, H = 700, 800
canvas = rt.TCanvas("c2", "c2", 50, 50, W, H)

# Define the main plot area
mainPlotHeight = 1  # Adjust as needed
canvas.SetWindowSize(W, int(H * (1 + (1 - mainPlotHeight))))  # Adjust window size based on main and ratio plot heights

# Create main histogram for demonstration
h = rt.TH1F("h", "h; mass (GeV); Events", 80, 70, 110)
h.SetMaximum(260)
h.GetXaxis().SetTitle("mass (GeV)")  # X axis label for main plot
h.GetYaxis().SetTitle("Events")     # Y axis label for main plot
h.Draw()

# Open the ROOT file and get histograms
file = rt.TFile("histo.root", "READ")
data = file.Get("data")
MC = file.Get("MC")

# Draw MC histogram with a solid line
MC.SetLineColor(rt.kRed)
MC.SetLineStyle(1)
MC.Draw("HIST,same")

# Draw data histogram with markers
data.SetMarkerStyle(20)
data.SetMarkerSize(1.0)
data.Draw("P,same")

# Calculate maximum value of main histogram for scaling ratio plot
maxMain = max(h.GetMaximum(), MC.GetMaximum(), data.GetMaximum())

# Create a pad for the ratio plot
ratioPad = rt.TPad("ratioPad", "ratioPad", 0., 0., 1., 0.3)
ratioPad.SetTopMargin(0.05)
ratioPad.SetBottomMargin(0.3)  # Adjust bottom margin to leave space for main plot
ratioPad.Draw()
ratioPad.cd()

# Create the ratio histogram
ratio = data.Clone("ratio")
ratio.Divide(MC)
ratio.SetMarkerStyle(20)
ratio.SetMarkerSize(1.0)
ratio.SetStats(0)
ratio.SetTitle("")
ratio.GetYaxis().SetTitle("Data/MC")
ratio.GetYaxis().SetTitleOffset(0.5)
ratio.GetYaxis().SetLabelSize(0.08)
ratio.GetXaxis().SetLabelSize(0.08)
ratio.SetMaximum(2.0)  # Adjust maximum range of ratio plot if needed
ratio.SetMinimum(0.5)  # Adjust minimum range of ratio plot if needed
ratio.Draw("P")

# Draw a horizontal line at y=1 for reference
line = rt.TLine(h.GetXaxis().GetXmin(), 1, h.GetXaxis().GetXmax(), 1)
line.SetLineStyle(2)
line.Draw()

# Go back to the main canvas to update and display
canvas.cd()

# Update the canvas
canvas.Update()

# Save the canvas as a file or display it
canvas.SaveAs("canvas_with_ratio.png")
canvas.Draw()
