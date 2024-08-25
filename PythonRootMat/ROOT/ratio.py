import ROOT  
import CMS_lumi, tdrstyle
import array

#set the tdr style
tdrstyle.setTDRStyle()

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

H_ref = 600; 
W_ref = 800; 
W = W_ref
H  = H_ref

iPeriod = 3

# references for T, B, L, R
T = 0.08*H_ref
B = 0.12*H_ref 
L = 0.12*W_ref
R = 0.04*W_ref


# Set modern style
'''
ROOT.gStyle.SetOptTitle(0)        # Disable title
ROOT.gStyle.SetOptStat(0)         # Disable statistics box
ROOT.gStyle.SetLabelFont(42, "XYZ")
ROOT.gStyle.SetTitleFont(42, "XYZ")
ROOT.gStyle.SetTitleOffset(1.1, "Y")
ROOT.gStyle.SetTitleSize(0.05, "XYZ")
ROOT.gStyle.SetLabelSize(0.04, "XYZ")
'''
# Create canvas and histogram
c1 = ROOT.TCanvas("c1", "Fit Residual Simple", 800, 600)
h1 = ROOT.TH1D("h1", "Distribution with Fit", 50, -5, 5)


c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetFrameFillStyle(0)
c1.SetFrameBorderMode(0)
c1.SetLeftMargin( L/W )
c1.SetRightMargin( R/W )
c1.SetTopMargin( T/H )
c1.SetBottomMargin( B/H )
c1.SetTickx(0)
c1.SetTicky(0)

# Fill histogram with random data
h1.FillRandom("gaus", 2000)

# Fit histogram with a Gaussian function (option "0" means no draw)
h1.Fit("gaus", "0")

# Set labels for x and y axes
h1.GetXaxis().SetTitle("X")
h1.GetYaxis().SetTitle("Counts")

# Customize histogram appearance
h1.SetLineColor(ROOT.kBlue)
h1.SetMarkerColor(ROOT.kBlue)
h1.SetMarkerStyle(ROOT.kFullCircle)
h1.SetLineWidth(2)

# Draw histogram
h1.Draw()

# Create TRatioPlot for ratio plot
rp1 = ROOT.TRatioPlot(h1)

# Set draw option for the histogram in the ratio plot
rp1.SetH1DrawOpt("E")

# Customize ratio plot appearance
rp1.SetConfidenceIntervalColors(ROOT.kRed, ROOT.kGreen)

# Check if lower reference graph exists before setting properties
if rp1.GetLowerRefGraph():
    rp1.GetLowerRefGraph().SetMinimum(-3)
    rp1.GetLowerRefGraph().SetMaximum(3)
    rp1.GetLowerRefGraph().SetLineColor(ROOT.kBlue)
    rp1.GetLowerRefGraph().SetMarkerColor(ROOT.kBlue)
    rp1.GetLowerRefGraph().SetMarkerStyle(ROOT.kFullCircle)
    rp1.GetLowerRefGraph().SetLineWidth(2)
    rp1.GetLowerRefGraph().SetTitle("Residuals")
    rp1.GetLowerRefGraph().GetYaxis().SetTitle("Data/Fit")
    rp1.GetLowerRefGraph().GetYaxis().SetTitleSize(0.05)
    rp1.GetLowerRefGraph().GetYaxis().SetTitleOffset(1.2)
    rp1.GetLowerRefGraph().GetXaxis().SetTitle("X")
    rp1.GetLowerRefGraph().GetXaxis().SetTitleSize(0.05)
    rp1.GetLowerRefGraph().GetXaxis().SetTitleOffset(0.9)

# Draw ratio plot
rp1.Draw()

# Set legend
legend = ROOT.TLegend(0.65, 0.75, 0.9, 0.9)
legend.AddEntry(h1, "Data", "lep")
legend.AddEntry(rp1.GetUpperPad().FindObject("ratio_hist"), "Ratio", "lep")
legend.SetTextSize(0.03)
legend.Draw()

# Show the canvas

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c1, iPeriod, iPos)

c1.cd()
c1.Update()
c1.RedrawAxis()
c1.Draw()

# Keep the program running to view the plot
ROOT.gApplication.Run()
