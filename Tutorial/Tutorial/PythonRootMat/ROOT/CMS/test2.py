import ROOT as rt
import CMS_lumi, tdrstyle

tdrstyle.setTDRStyle()

# Create histograms
h1 = rt.TH1F("h1", "Events", 100, -5, 5)
h2 = rt.TH1F("h2", "h2", 100, -5, 5)
h1.FillRandom("gaus")
h2.FillRandom("gaus")

def plotratio(h1, h2):
    # Define the Canvas
    c = rt.TCanvas("c", "canvas", 800, 800)

    # Upper plot will be in pad1
    pad1 = rt.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0) # Upper and lower plot are joined
    pad1.SetGridx()         # Vertical grid
    pad1.Draw()             # Draw the upper pad: pad1
    pad1.cd()               # pad1 becomes the current pad
    h1.SetStats(0)          # No statistics on upper plot
    h1.Sumw2()
    h1.Scale(1. / h1.Integral())
    h1.Draw("histo")               # Draw h1

    h2.Sumw2()
    h2.Scale(1. / h2.Integral())
    h2.Draw("histo same")         # Draw h2 on top of h1

    # Do not draw the Y axis label on the upper plot and redraw a small
    # axis instead, in order to avoid the first label (0) to be clipped.
    h1.GetYaxis().SetLabelSize(0.)
    axis = rt.TGaxis(-5, 0.1, -5, 1., 0.1, 1., 510, "")
    axis.SetLabelFont(43) # Absolute font size in pixel (precision 3)
    axis.SetLabelSize(15)
    axis.Draw()

    # lower plot will be in pad
    c.cd()          # Go back to the main canvas before defining pad2
    pad2 = rt.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.2)
    pad2.SetGridx()  # vertical grid
    pad2.Draw()
    pad2.cd()       # pad2 becomes the current pad

    # Define the ratio plot
    h3 = h1.Clone("h3")
    h3.SetLineColor(1)
    h3.SetMinimum(0.8)  # Define Y ..
    h3.SetMaximum(1.35) # .. range
    h3.Sumw2()
    h3.SetStats(0)      # No statistics on lower plot
    h3.Divide(h2)
    h3.SetMarkerStyle(21)
    h3.Draw("ep")       # Draw the ratio plot

    # h1 settings
    h1.SetLineColor(5)
    h1.SetLineWidth(2)

    # Y axis h1 plot settings
    h1.GetYaxis().SetTitleSize(20)
    h1.GetYaxis().SetTitleFont(43)
    h1.GetYaxis().SetTitleOffset(1.55)

    # h2 settings
    h2.SetLineColor(2)
    h2.SetLineWidth(2)

    # Ratio plot (h3) settings
    h3.SetTitle("") # Remove the ratio title

    # Y axis ratio plot settings
    h3.GetYaxis().SetTitle("ratio h1/h2 ")
    h3.GetXaxis().SetTitle("h1 ")
    h3.GetYaxis().SetNdivisions(505)
    h3.GetYaxis().SetTitleSize(20)
    h3.GetYaxis().SetTitleFont(43)
    h3.GetYaxis().SetTitleOffset(1.55)
    h3.GetYaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
    h3.GetYaxis().SetLabelSize(15)

    # X axis ratio plot settings
    h3.GetXaxis().SetTitleSize(20)
    h3.GetXaxis().SetTitleFont(43)
    h3.GetXaxis().SetTitleOffset(2.5)
    h3.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
    h3.GetXaxis().SetLabelSize(15)

    # Save the canvas as a file
    c.SaveAs("plot.png")

plotratio(h1, h2)
