import ROOT

# Open the ROOT file and get the histograms
file_path = "../sorted_mass.root"
file = ROOT.TFile(file_path, "READ")

Kaon_hist = file.Get("histKaon")
Pion_hist = file.Get("histPion")

# Create a canvas and divide it into 3 pads (1 row, 3 columns)
canvas = ROOT.TCanvas("canvas", "Mass Distributions", 1200, 600)
canvas.Divide(3, 1)  # 3 pads in a single row

# Pad 1: Plot Pion and Kaon histograms
canvas.cd(1)  # Switch to Pad 1
Pion_hist.SetLineColor(ROOT.kBlue)
Kaon_hist.SetLineColor(ROOT.kRed)
Pion_hist.SetStats(0)
Kaon_hist.SetStats(0)
Kaon_hist.Draw("HIST")
Pion_hist.Draw("HIST SAME")
Kaon_hist.SetTitle("Pion and Kaon Mass Distribution")
Pion_hist.GetYaxis().SetTitle("Events")
Pion_hist.GetXaxis().SetTitle("Mass (GeV/c^2)")

# Add a legend to Pad 1
legend1 = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend1.AddEntry(Pion_hist, "massPion", "l")
legend1.AddEntry(Kaon_hist, "massKaon", "l")
legend1.Draw()

# Pad 2: Compute and plot the ratio of Pion/Kaon histograms
canvas.cd(2)  # Switch to Pad 2
ratio_hist = Pion_hist.Clone("ratio_hist")
ratio_hist.Divide(Kaon_hist)
ratio_hist.SetLineColor(ROOT.kBlack)
ratio_hist.SetTitle("Ratio of Pion/Kaon")
ratio_hist.GetYaxis().SetTitle("Ratio")
ratio_hist.GetXaxis().SetTitle("Mass (GeV/c^2)")
ratio_hist.Draw()

# Pad 3: Fit the Pion histogram with a Gaussian
canvas.cd(3)  # Switch to Pad 3
Pion_hist.Fit("gaus")  # Fit with a Gaussian function
Pion_hist.Draw()

# Update the canvas
canvas.Update()

# Save the canvas to a file (e.g., PNG, PDF, etc.)
canvas.SaveAs("output_plot.png")  # Save as PNG
# You can also save it as PDF, ROOT file, or other formats:
# canvas.SaveAs("output_plot.pdf")
# canvas.SaveAs("output_plot.root")
