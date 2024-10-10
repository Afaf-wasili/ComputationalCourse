'''
Question3: (K1, S1, S3 & S4)
A. Modify this code to plot the ptsumf from the ROOT file for both signal and background
B. Define the product between the efficiency and purity
C. Save the plot as pdf
'''


import ROOT

ROOT.gROOT.SetStyle("ATLAS")
ROOT.gROOT.ForceStyle()

ROOT.gStyle.SetLabelFont(22, "X")
ROOT.gStyle.SetLabelFont(22, "Y")
ROOT.gStyle.SetTitleFont(22, "X")
ROOT.gStyle.SetTitleFont(22, "Y")

ROOT.gStyle.SetLabelSize(0.03, "X")
ROOT.gStyle.SetLabelSize(0.03, "Y")
ROOT.gStyle.SetTitleSize(0.04, "X")
ROOT.gStyle.SetTitleSize(0.04, "Y")
ROOT.gStyle.SetMarkerSize(0.5)

ROOT.gStyle.SetLegendFont(22)

file = ROOT.TFile("mlpHiggs.root", "READ")
sig_tree = file.Get("sig_filtered")
bg_tree = file.Get("bg_filtered")

total_signal_events = sig_tree.GetEntries()
total_background_events = bg_tree.GetEntries()

efficiency_graph = ROOT.TGraphErrors()
purity_graph = ROOT.TGraphErrors()

selection_cuts = range(35, 180)

for i in selection_cuts:
    signal_entry_count = 0
    background_entry_count = 0

    for j in range(total_signal_events):
        sig_tree.GetEntry(j)
        if sig_tree.acolin >= i:
            signal_entry_count += 1

    for k in range(total_background_events):
        bg_tree.GetEntry(k)
        if bg_tree.acolin >= i:
            background_entry_count += 1

    if signal_entry_count == 0 or total_signal_events == 0:
        continue
    efficiency = signal_entry_count / total_signal_events
    efficiency_error = (efficiency * (1 - efficiency) / total_signal_events) ** 0.5

    total_valid_events = signal_entry_count + background_entry_count
    purity = signal_entry_count / total_valid_events
    purity_error = (purity * (1 - purity) / total_valid_events) ** 0.5

    efficiency_graph.SetPoint(efficiency_graph.GetN(), i, efficiency)
    efficiency_graph.SetPointError(efficiency_graph.GetN() - 1, 0, efficiency_error)
    purity_graph.SetPoint(purity_graph.GetN(), i, purity)
    purity_graph.SetPointError(purity_graph.GetN() - 1, 0, purity_error)

efficiency_graph.GetXaxis().SetTitle("")
efficiency_graph.GetYaxis().SetTitle("Signal Efficiency / Purity")
efficiency_graph.SetLineColor(ROOT.kBlue)
efficiency_graph.SetMarkerStyle(20)
efficiency_graph.SetMarkerColor(ROOT.kBlue)

purity_graph.SetLineColor(ROOT.kRed)
purity_graph.SetMarkerStyle(21)
purity_graph.SetMarkerColor(ROOT.kRed)

canvas = ROOT.TCanvas("canvas", "", 800, 600)
canvas.SetGrid()
efficiency_graph.Draw("ALP")
purity_graph.Draw("LP")

legend = ROOT.TLegend(0.17, 0.17, 0.3, 0.34)
legend.SetHeader("made by ....")
legend.AddEntry(efficiency_graph, "Efficiency", "alp")
legend.AddEntry(purity_graph, "Purity", "lp")
legend.Draw()

canvas.Update()
ROOT.gApplication.Run()

file.Close()
