import ROOT as rt

# Open the ROOT file and get histograms
file = rt.TFile("histo.root", "READ")
data = file.Get("data")
MC = file.Get("MC")

# Create a canvas
canvas = rt.TCanvas("canvas", "canvas", 800, 800)

# Upper pad (main plot)
pad1 = rt.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
pad1.SetBottomMargin(0.05)
#pad1.Draw()
#pad1.cd()

# Draw data histogram with blue color and solid line
data.SetLineColor(rt.kBlue)
data.SetLineStyle(1)  # Solid line style
data.Draw()

# Draw MC histogram with red color and dashed line
MC.SetLineColor(rt.kRed)
MC.SetLineStyle(1)  # Dashed line style
MC.Draw("SAME")

# Add legend
legend = rt.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(data, "Data", "l")
legend.AddEntry(MC, "MC", "l")
legend.Draw()

# Adjust axis labels and titles
data.GetXaxis().SetTitle("X-axis Title")
data.GetYaxis().SetTitle("Y-axis Title")

# Update the canvas
canvas.Update()

# Lower pad (ratio plot)
canvas.cd()
pad2 = rt.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
pad2.SetTopMargin(0.05)
pad2.SetBottomMargin(0.2)
pad2.Draw()
pad2.cd()

# Calculate the ratio plot
ratio = rt.TRatioPlot(data, MC)
ratio.Draw()

# Customize ratio plot if needed (axis labels, range, etc.)
ratio.GetLowerRefYaxis().SetTitle("Data/MC")
ratio.GetLowerRefGraph().SetMinimum(0.5)
ratio.GetLowerRefGraph().SetMaximum(1.5)

# Update the canvas
canvas.Update()

# Save the canvas to a file if needed
canvas.SaveAs("plot.pdf")

# Optionally, keep the program running
canvas.WaitPrimitive()
