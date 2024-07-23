import ROOT as rt
import CMS_lumi, tdrstyle

# Set TDR style                                                                                                                                                                          
tdrstyle.setTDRStyle()

# Set canvas dimensions                                                                                                                                                                  
W, H = 800, 600
canvas = rt.TCanvas("c2", "c2", 50, 50, W, H)

# Create a histogram for demonstration                                                                                                                                                   
h = rt.TH1F("h", "h; mass (GeV); Events", 80, 70, 110)
h.SetMaximum(260)
h.GetXaxis().SetTitle("mass (GeV)")
h.GetYaxis().SetTitle("Events")
h.Draw()

# Open the ROOT file and get histograms                                                                                                                                                  
file = rt.TFile("histo.root", "READ")
data = file.Get("data")
MC = file.Get("MC")

# Draw MC histogram with a solid line and add to legend                                                                                                                                  
MC.SetLineColor(rt.kRed)
MC.SetLineStyle(1)
MC.Draw("HIST,same")
legend = rt.TLegend(0.6, 0.7, 0.9, 0.85)
legend.AddEntry(MC, "MC", "f")

# Draw data histogram with markers and add to legend                                                                                                                                     
data.SetMarkerStyle(20)
data.SetMarkerSize(1.0)
data.Draw("HIST,same")
legend.AddEntry(data, "Data", "l")

# Set legend styles                                                                                                                                                                      
legend.SetBorderSize(0)  # Remove border around legend                                                                                                                                   
legend.SetTextSize(0.04)
legend.Draw()

# Remove statistics box                                                                                                                                                                  
h.SetStats(0)  # Turn off statistics box for histogram h                                                                                                                                #add CL
CL_low = [0.0] * h.GetNbinsX()  # Example: Replace with actual lower CL values
CL_high = [10.0] * h.GetNbinsX()  # Example: Replace with actual upper CL values
n_bins = h.GetNbinsX()
gr = rt.TGraphAsymmErrors(n_bins)
for i in range(n_bins):
    x = h.GetBinCenter(i+1)
    y = h.GetBinContent(i+1)
    exl = h.GetBinWidth(i+1) / 2.0
    exh = h.GetBinWidth(i+1) / 2.0
    eyl = y - CL_low[i]
    eyh = CL_high[i] - y
    gr.SetPoint(i, x, y)
    gr.SetPointError(i, exl, exh, eyl, eyh)
    gr.SetFillColor(rt.kYellow)  # Fill color for the band
    gr.SetFillStyle(3001)        # Fill style (solid by default)
    gr.Draw("e2 same")           # Draw as filled area ("e2" option)
    legend.AddEntry(gr, "CL Band", "f")
#    legend.Draw()


# Update canvas and save plot                                                                                                                                                            
canvas.Update()
canvas.SaveAs("plot.pdf")

# Wait for user input to end                                                                                                                                                             
input("Press Enter to end")
