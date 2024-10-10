'''
Question1: (K1, S1 , S2 & S4 )
A. Modifing this code to define the ptsumf variable to plot it from the provided ROOT file, creating a 2D plot between the signal and background
B. Rebining the y and x axis to be 200 and change the range of x and y 
C. Naming the x and y axis 
D. Adding your name into the legend, and save the plot as pdf
'''
import ROOT

def fill2DHistogram():
    c = ROOT.TCanvas("c", "Background vs Signal", 800, 600)
    
    ROOT.gROOT.SetStyle("ATLAS")
    ROOT.gROOT.ForceStyle()

    ROOT.gStyle.SetLabelFont(22, "X")
    ROOT.gStyle.SetLabelFont(22, "Y")
    ROOT.gStyle.SetLabelFont(22, "Z")
    ROOT.gStyle.SetTitleFont(22, "X")
    ROOT.gStyle.SetTitleFont(22, "Y")
    ROOT.gStyle.SetTitleFont(22, "Z")

    ROOT.gStyle.SetLabelSize(0.03, "X")
    ROOT.gStyle.SetLabelSize(0.03, "Y")
    ROOT.gStyle.SetLabelSize(0.03, "Z")
    ROOT.gStyle.SetTitleSize(0.04, "X")
    ROOT.gStyle.SetTitleSize(0.04, "Y")
    ROOT.gStyle.SetTitleSize(0.04, "Z")

    ROOT.gStyle.SetMarkerSize(0.5)
    ROOT.gStyle.SetPalette(ROOT.kRainBow)

    c.SetRightMargin(0.20)
    c.SetLeftMargin(0.12)
    c.SetBottomMargin(0.12)

    file = ROOT.TFile.Open("mlpHiggs.root")
    sig_tree = file.Get("sig_filtered")
    bg_tree = file.Get("bg_filtered")

    hist_2d = ROOT.TH2F("", "",
                         100, 80, 180,
                         100, 80, 180)

    for j in range(bg_tree.GetEntries()):
        bg_tree.GetEntry(j)
        for i in range(sig_tree.GetEntries()):
            sig_tree.GetEntry(i)
            hist_2d.Fill(bg_tree.acolin, sig_tree.acolin)

    hist_2d.Draw("COLZ")
    legend = ROOT.TLegend(0.1, 0.92, 0.9, 0.98)
    legend.SetHeader("Made by ", "C")  # Centered header
    legend.SetFillStyle(0)  # Make legend transparent
    legend.Draw()

    c.Update()

    file.Close()

    ROOT.gApplication.Run()

fill2DHistogram()
