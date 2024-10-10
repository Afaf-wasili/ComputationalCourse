import ROOT

def fill2DHistogram():
    # Create the canvas before applying other styles
    c = ROOT.TCanvas("c", "Background vs Signal", 800, 600)

    # Set the ATLAS style and force it
    ROOT.gROOT.SetStyle("ATLAS")
    ROOT.gROOT.ForceStyle()

    # Set font for axis titles and labels
    ROOT.gStyle.SetLabelFont(22, "X")
    ROOT.gStyle.SetLabelFont(22, "Y")
    ROOT.gStyle.SetLabelFont(22, "Z")
    ROOT.gStyle.SetTitleFont(22, "X")
    ROOT.gStyle.SetTitleFont(22, "Y")
    ROOT.gStyle.SetTitleFont(22, "Z")

    # Set size of axis titles and labels
    ROOT.gStyle.SetLabelSize(0.03, "X")
    ROOT.gStyle.SetLabelSize(0.03, "Y")
    ROOT.gStyle.SetLabelSize(0.03, "Z")
    ROOT.gStyle.SetTitleSize(0.04, "X")
    ROOT.gStyle.SetTitleSize(0.04, "Y")
    ROOT.gStyle.SetTitleSize(0.04, "Z")

    # Set color palette and marker size
    ROOT.gStyle.SetMarkerSize(0.5)
    ROOT.gStyle.SetPalette(ROOT.kRainBow)

    # Adjust canvas margins after its creation
    c.SetRightMargin(0.20)  # Increase margin to fit the Z-axis labels
    c.SetLeftMargin(0.12)   # Adjust left margin for balance
    c.SetBottomMargin(0.12) # Adjust bottom margin for X-axis labels

    # Open the ROOT file and retrieve the trees
    file = ROOT.TFile.Open("mlpHiggs.root")
    sig_tree = file.Get("sig_filtered")
    bg_tree = file.Get("bg_filtered")

    # Create a 2D histogram
    hist_2d = ROOT.TH2F("hist_2d", "Background vs Signal;Background;Signal",
                         100, 80, 180,
                         100, 80, 180)

    # Loop over the trees and fill the histogram
    for j in range(bg_tree.GetEntries()):
        bg_tree.GetEntry(j)
        for i in range(sig_tree.GetEntries()):
            sig_tree.GetEntry(i)
            hist_2d.Fill(bg_tree.acolin, sig_tree.acolin)  # Replace with actual variable names

    # Draw the histogram on the canvas
    hist_2d.Draw("COLZ")

    # Adjust the Z-axis labels and title
    hist_2d.GetZaxis().SetLabelSize(0.03)
    hist_2d.GetZaxis().SetTitleSize(0.04)
    hist_2d.GetZaxis().SetTitleOffset(1.3)

    # Update the canvas
    c.Update()

    # Close the file
    file.Close()

    # Optionally save the canvas
    # c.SaveAs("Plots/Background_Signal_2D_Histogram.png")

    # Keep the application running to display the canvas
    ROOT.gApplication.Run()

# Run the function
fill2DHistogram()
