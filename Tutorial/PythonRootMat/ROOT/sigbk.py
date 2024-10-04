import ROOT

# Open the ROOT file
file_path = "mlpHiggs.root"  # Ensure this is the correct path
file = ROOT.TFile(file_path, "READ")

# Get the trees for background and signal
bg_tree = file.Get("bg_filtered")
sig_tree = file.Get("sig_filtered")

# Create histograms for the 'acolin' variable from both trees
bg_hist = ROOT.TH1F("bg_acolin", "Acollinearity - Background",50, 30, 180)
sig_hist = ROOT.TH1F("sig_acolin", "Acollinearity - Signal", 50, 30, 180)

sig_hist.GetYaxis().SetRangeUser(0, 200)
# Project the 'acolin' variable into the histograms
bg_tree.Draw("acolin >> bg_acolin ")
sig_tree.Draw("acolin >> sig_acolin")

# Set axis titles
#bg_hist.SetXTitle("mass  GeV/C^2")
#bg_hist.SetYTitle("Number of Events")
sig_hist.SetXTitle("mass")
sig_hist.SetYTitle("Number of Events")
 
# Remove the statistical box
bg_hist.SetStats(0)
sig_hist.SetStats(0)

# Create a canvas
canvas = ROOT.TCanvas("canvas", "Signal vs Background: acolin", 800, 600)

# Set histogram attributes (line colors, etc.)
bg_hist.SetLineColor(ROOT.kRed)  # Set background histogram color to red
sig_hist.SetLineColor(ROOT.kBlue)  # Set signal histogram color to blue

# Draw the histograms
sig_hist.Draw("HIST")
bg_hist.Draw("HIST SAME")



# Add a legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(bg_hist, "Background", "l")
legend.AddEntry(sig_hist, "Signal", "l")
legend.Draw()

# Update the canvas to show the plots
canvas.Update()
#canvas.SaveAs("Plots/sigkg.png")
# Keep the application running to display the canvas
ROOT.gApplication.Run()

# Close the ROOT file
file.Close()
