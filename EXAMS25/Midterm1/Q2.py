'''
Question2: (K1, S1 & S4)
A. Add the order to plot these two histograms in the same canvas, the order is still missing
B. Changing the variables to plot ptsumf from the ROOT file for both signal and background
C. Changing the range of x and y and naming the x and y axis 
'''

import ROOT

def fill1DHistogram():
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

    bg_hist = ROOT.TH1F("", "", 50, 30, 180)
    sig_hist = ROOT.TH1F("", "", 50, 30, 180)

    for j in range(bg_tree.GetEntries()):
        bg_tree.GetEntry(j)
        for i in range(sig_tree.GetEntries()):
            sig_tree.GetEntry(i)
            sig_hist.Fill(sig_tree.acolin)
            bg_hist.Fill(bg_tree.acolin)


    bg_hist.SetStats(0)
    sig_hist.SetStats(0)

    bg_hist.SetLineColor(ROOT.kRed)
    sig_hist.SetLineColor(ROOT.kBlue)


    # Add a legend with a centered header
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.SetHeader("Made by ....", "C")  # Centered header
    legend.AddEntry(bg_hist, "Background", "l")
    legend.AddEntry(sig_hist, "Signal", "l")
    legend.Draw()

    c.Update()

    # Keep the application running to display the canvas
    ROOT.gApplication.Run()

    file.Close()

fill1DHistogram()
