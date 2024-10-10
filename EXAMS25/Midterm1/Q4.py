'''
Question4: (S1, S3 & S4)
A. Fit the data using gussian function 
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

file_path = "mlpHiggs.root"
file = ROOT.TFile(file_path, "READ")

bg_tree = file.Get("bg_filtered")

bg_hist = ROOT.TH1F("", "", 150, 0, 0.5)

for j in range(bg_tree.GetEntries()):
    bg_tree.GetEntry(j)
    bg_hist.Fill(bg_tree.ptsumf)

bg_hist.SetStats(0)

canvas = ROOT.TCanvas("canvas", "", 800, 600)

bg_hist.Draw("HIST")

'''
'''
mean = gauss.GetParameter(1)
sigma = gauss.GetParameter(2)
mean_error = gauss.GetParError(1)
sigma_error = gauss.GetParError(2)

legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.SetHeader("made by ....")
legend.AddEntry(bg_hist, "background", "l")
legend.AddEntry(gauss, "Gaussian Fit", "l")
legend.AddEntry("", f"#mu: {mean:.2f} #pm {mean_error:.3f}", "")
legend.AddEntry("", f"#sigma: {sigma:.2f} #pm {sigma_error:.3f}", "")
legend.Draw()

canvas.Update()
ROOT.gApplication.Run()
file.Close()
