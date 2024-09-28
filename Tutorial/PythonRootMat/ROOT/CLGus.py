
import ROOT
import numpy as np

# Initial setup
config = 0
timingfactor = 0.98
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.TGaxis.SetExponentOffset(0.02, -0.05, "x")
ROOT.gROOT.SetBatch()

# Define palette using numpy for better compatibility
stops = np.array([0.0000, 0.1250, 0.2500, 0.3750, 0.5000, 0.6250, 0.7500, 0.8750, 1.0000], dtype='float64')
Red = np.array([26./255., 51./255., 43./255., 33./255., 28./255., 35./255., 74./255., 144./255., 246./255.], dtype='float64')
Green = np.array([9./255., 24./255., 55./255., 87./255., 118./255., 150./255., 180./255., 200./255., 222./255.], dtype='float64')
Blue = np.array([30./255., 96./255., 112./255., 114./255., 112./255., 101./255., 72./255., 35./255., 0./255.], dtype='float64')

# Create gradient color table
FI = ROOT.TColor.CreateGradientColorTable(9, stops, Red, Green, Blue, 255, 1.0)

# Create MyPalette as a list of integers
MyPalette = [FI + i for i in range(255)]
MyPalette = np.array(MyPalette, dtype='int32')  # Convert to numpy int32 array

# Palette settings
ROOT.gStyle.SetPalette(255, MyPalette)

# Style settings
ROOT.gStyle.SetTitleOffset(0.9, "Y")
ROOT.gStyle.SetTitleOffset(0.9, "X")
ROOT.gStyle.SetTitleSize(0.06, "XYZ")
ROOT.gStyle.SetLabelSize(0.05, "XYZ")
ROOT.gStyle.SetMarkerStyle(20)
ROOT.gStyle.SetHistLineColor(1)
ROOT.gStyle.SetMarkerColor(1)
ROOT.gStyle.SetMarkerSize(0.6)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle()
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetPalette(58)  # Set specific palette
ROOT.TGaxis.SetMaxDigits(3)
ROOT.gStyle.SetNumberContours(99)
ROOT.gStyle.SetNdivisions(510, "xyz")

# Canvas and pad settings
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetFrameFillColor(0)
ROOT.gStyle.SetPadColor(0)
ROOT.gStyle.SetHistLineWidth(3)
ROOT.gStyle.SetHistLineColor(1)
ROOT.gStyle.SetHistLineStyle(1)
ROOT.gStyle.SetHistFillColor(0)
ROOT.gStyle.SetHistFillStyle(0)
ROOT.gStyle.SetLabelFont(132, "xyz")
ROOT.gStyle.SetLabelOffset(0.005, "xyz")
ROOT.gStyle.SetLabelSize(0.05, "xyz")

# Title settings
ROOT.gStyle.SetTitleFont(132, "xyz")
ROOT.gStyle.SetTitleOffset(0.9, "xyz")
ROOT.gStyle.SetTitleSize(0.05)
ROOT.gStyle.SetLegendFillColor(0)
ROOT.gStyle.SetLegendFont(132)
ROOT.gStyle.SetLegendTextSize(0.04)

# Statistics settings
ROOT.gStyle.SetStatColor(0)
ROOT.gStyle.SetStatFont(132)
ROOT.gStyle.SetStatFontSize(0.04)
ROOT.gStyle.SetStatFormat("")

# Create custom style
kunoStyle = ROOT.TStyle("kunoStyle", "Style for Kuno Plots")
kunoStyle.SetOptStat(0)
kunoStyle.SetOptFit()
kunoStyle.SetPalette(58)
ROOT.TGaxis.SetMaxDigits(3)
kunoStyle.SetNumberContours(99)
kunoStyle.SetNdivisions(510, "xyz")
kunoStyle.SetCanvasColor(0)
kunoStyle.SetFrameFillColor(0)
kunoStyle.SetPadColor(0)

# Finalize style settings
kunoStyle.SetHistLineWidth(3)
kunoStyle.SetLabelFont(132, "X")
kunoStyle.SetLabelSize(0.05, "xyz")
kunoStyle.SetTitleFont(132, "Y")
kunoStyle.SetTitleOffset(1.2, "xyz")
kunoStyle.SetTitleSize(0.05)
kunoStyle.SetLegendFillColor(0)
kunoStyle.SetLegendFont(132)
kunoStyle.SetLegendTextSize(0.04)
kunoStyle.SetStatColor(0)
kunoStyle.SetStatFont(132)
kunoStyle.SetStatFontSize(0.04)
kunoStyle.SetStatFormat("")

# Apply the custom style
ROOT.gROOT.SetStyle("kunoStyle")

# Additional canvas settings
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptDate(0)
ROOT.gStyle.SetLabelSize(0.03, "xyz")  # size of axis value font
ROOT.gStyle.SetTitleSize(0.035, "xyz")  # size of axis title font
ROOT.gStyle.SetTitleFont(22, "xyz")  # font option
ROOT.gStyle.SetLabelFont(22, "xyz")
ROOT.gStyle.SetTitleOffset(1.2, "y")  # default canvas options
ROOT.gStyle.SetCanvasDefW(500)
ROOT.gStyle.SetCanvasDefH(500)
ROOT.gStyle.SetCanvasColor(0)  # canvas...
ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetCanvasBorderSize(0)
ROOT.gStyle.SetPadLeftMargin(0.133)
ROOT.gStyle.SetPadRightMargin(0.1)

ROOT.gStyle.SetPadBottomMargin(0.1)  # margins...
ROOT.gStyle.SetPadTopMargin(0.1)
ROOT.gStyle.SetPadLeftMargin(0.1)
ROOT.gStyle.SetPadRightMargin(0.1)
ROOT.gStyle.SetPadGridX(1)  # grids,tickmarks
ROOT.gStyle.SetPadGridY(1)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetPaperSize(20, 24)  # US letter size



'''
import ROOT
import numpy as np

# Initial setup
config = 0
timingfactor = 0.98
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.TGaxis.SetExponentOffset(0.02, -0.05, "x")
ROOT.gROOT.SetBatch()

# Define palette using numpy for better compatibility
stops = np.array([0.0000, 0.1250, 0.2500, 0.3750, 0.5000, 0.6250, 0.7500, 0.8750, 1.0000], dtype='float64')
Red = np.array([26./255., 51./255., 43./255., 33./255., 28./255., 35./255., 74./255., 144./255., 246./255.], dtype='float64')
Green = np.array([9./255., 24./255., 55./255., 87./255., 118./255., 150./255., 180./255., 200./255., 222./255.], dtype='float64')
Blue = np.array([30./255., 96./255., 112./255., 114./255., 112./255., 101./255., 72./255., 35./255., 0./255.], dtype='float64')

# Create gradient color table
FI = ROOT.TColor.CreateGradientColorTable(9, stops, Red, Green, Blue, 255, 1.0)

# Palette settings
MyPalette = [FI + i for i in range(255)]
ROOT.gStyle.SetPalette(255, MyPalette)

# Style settings
ROOT.gStyle.SetTitleOffset(0.9, "Y")
ROOT.gStyle.SetTitleOffset(0.9, "X")
ROOT.gStyle.SetTitleSize(0.06, "XYZ")
ROOT.gStyle.SetLabelSize(0.05, "XYZ")
ROOT.gStyle.SetMarkerStyle(20)
ROOT.gStyle.SetHistLineColor(1)
ROOT.gStyle.SetMarkerColor(1)
ROOT.gStyle.SetMarkerSize(0.6)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle()
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetPalette(58)  # Set specific palette
ROOT.TGaxis.SetMaxDigits(3)
ROOT.gStyle.SetNumberContours(99)
ROOT.gStyle.SetNdivisions(510, "xyz")

# Canvas and pad settings
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetFrameFillColor(0)
ROOT.gStyle.SetPadColor(0)
ROOT.gStyle.SetHistLineWidth(3)
ROOT.gStyle.SetHistLineColor(1)
ROOT.gStyle.SetHistLineStyle(1)
ROOT.gStyle.SetHistFillColor(0)
ROOT.gStyle.SetHistFillStyle(0)
ROOT.gStyle.SetLabelFont(132, "xyz")
ROOT.gStyle.SetLabelOffset(0.005, "xyz")
ROOT.gStyle.SetLabelSize(0.05, "xyz")

# Title settings
ROOT.gStyle.SetTitleFont(132, "xyz")
ROOT.gStyle.SetTitleOffset(0.9, "xyz")
ROOT.gStyle.SetTitleSize(0.05)
ROOT.gStyle.SetLegendFillColor(0)
ROOT.gStyle.SetLegendFont(132)
ROOT.gStyle.SetLegendTextSize(0.04)

# Statistics settings
ROOT.gStyle.SetStatColor(0)
ROOT.gStyle.SetStatFont(132)
ROOT.gStyle.SetStatFontSize(0.04)
ROOT.gStyle.SetStatFormat("")

# Create custom style
kunoStyle = ROOT.TStyle("kunoStyle", "Style for Kuno Plots")
kunoStyle.SetOptStat(0)
kunoStyle.SetOptFit()
kunoStyle.SetPalette(58)
ROOT.TGaxis.SetMaxDigits(3)
kunoStyle.SetNumberContours(99)
kunoStyle.SetNdivisions(510, "xyz")
kunoStyle.SetCanvasColor(0)
kunoStyle.SetFrameFillColor(0)
kunoStyle.SetPadColor(0)

# Finalize style settings
kunoStyle.SetHistLineWidth(3)
kunoStyle.SetLabelFont(132, "X")
kunoStyle.SetLabelSize(0.05, "xyz")
kunoStyle.SetTitleFont(132, "Y")
kunoStyle.SetTitleOffset(1.2, "xyz")
kunoStyle.SetTitleSize(0.05)
kunoStyle.SetLegendFillColor(0)
kunoStyle.SetLegendFont(132)
kunoStyle.SetLegendTextSize(0.04)
kunoStyle.SetStatColor(0)
kunoStyle.SetStatFont(132)
kunoStyle.SetStatFontSize(0.04)
kunoStyle.SetStatFormat("")

# Apply the custom style
ROOT.gROOT.SetStyle("kunoStyle")

# Additional canvas settings
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptDate(0)
ROOT.gStyle.SetLabelSize(0.03, "xyz")
ROOT.gStyle.SetTitleSize(0.035, "xyz")
ROOT.gStyle.SetTitleFont(22, "xyz")
ROOT.gStyle.SetLabelFont(22, "xyz")
ROOT.gStyle.SetTitleOffset(1.2, "y")
ROOT.gStyle.SetCanvasDefW(500)
ROOT.gStyle.SetCanvasDefH(500)
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetCanvasBorderSize(0)
ROOT.gStyle.SetPadLeftMargin(0.133)
ROOT.gStyle.SetPadRightMargin(0.1)
ROOT.gStyle.SetPadBottomMargin(0.1)
ROOT.gStyle.SetPadTopMargin(0.1)
ROOT.gStyle.SetPadLeftMargin(0.1)
ROOT.gStyle.SetPadRightMargin(0.1)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetPaperSize(20, 24)  # US letter size






# Initial setup
config = 0
timingfactor = 0.98
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.TGaxis.SetExponentOffset(0.02, -0.05, "x")
ROOT.gROOT.SetBatch()

# Define palette
MyPalette = [0] * 255
stops = [0.0000, 0.1250, 0.2500, 0.3750, 0.5000, 0.6250, 0.7500, 0.8750, 1.0000]
Red = [26./255., 51./255., 43./255., 33./255., 28./255., 35./255., 74./255., 144./255., 246./255.]
Green = [9./255., 24./255., 55./255., 87./255., 118./255., 150./255., 180./255., 200./255., 222./255.]
Blue = [30./255., 96./255., 112./255., 114./255., 112./255., 101./255., 72./255., 35./255., 0./255.]

# Create gradient color table
FI = ROOT.TColor.CreateGradientColorTable(9, stops, Red, Green, Blue, 255, 1.0)
# for i in range(255): MyPalette[i] = FI + i

ROOT.gStyle.SetPalette(255, MyPalette)

# Style settings
ROOT.gStyle.SetTitleOffset(0.9, "Y")
ROOT.gStyle.SetTitleOffset(0.9, "X")
ROOT.gStyle.SetTitleSize(0.06, "XYZ")
ROOT.gStyle.SetLabelSize(0.05, "XYZ")
ROOT.gStyle.SetMarkerStyle(20)
ROOT.gStyle.SetHistLineColor(1)
ROOT.gStyle.SetMarkerColor(1)
ROOT.gStyle.SetMarkerSize(0.6)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle()
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetPalette(58)  # Set specific palette
ROOT.TGaxis.SetMaxDigits(3)
ROOT.gStyle.SetNumberContours(99)
ROOT.gStyle.SetNdivisions(510, "xyz")

# Canvas and pad settings
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetFrameFillColor(0)
ROOT.gStyle.SetPadColor(0)
ROOT.gStyle.SetHistLineWidth(3)
ROOT.gStyle.SetHistLineColor(1)
ROOT.gStyle.SetHistLineStyle(1)
ROOT.gStyle.SetHistFillColor(0)
ROOT.gStyle.SetHistFillStyle(0)
ROOT.gStyle.SetLabelFont(132, "xyz")
ROOT.gStyle.SetLabelOffset(0.005, "xyz")
ROOT.gStyle.SetLabelSize(0.05, "xyz")

# Title settings
ROOT.gStyle.SetTitleFont(132, "xyz")
ROOT.gStyle.SetTitleOffset(0.9, "xyz")
ROOT.gStyle.SetTitleSize(0.05)
ROOT.gStyle.SetLegendFillColor(0)
ROOT.gStyle.SetLegendFont(132)
ROOT.gStyle.SetLegendTextSize(0.04)

# Statistics settings
ROOT.gStyle.SetStatColor(0)
ROOT.gStyle.SetStatFont(132)
ROOT.gStyle.SetStatFontSize(0.04)
ROOT.gStyle.SetStatFormat("")

# Create custom style
kunoStyle = ROOT.TStyle("kunoStyle", "Style for Kuno Plots")
kunoStyle.SetOptStat(0)
kunoStyle.SetOptFit()
kunoStyle.SetPalette(58)
ROOT.TGaxis.SetMaxDigits(3)
kunoStyle.SetNumberContours(99)
kunoStyle.SetNdivisions(510, "xyz")
kunoStyle.SetCanvasColor(0)
kunoStyle.SetFrameFillColor(0)
kunoStyle.SetPadColor(0)

# Finalize style settings
kunoStyle.SetHistLineWidth(3)
kunoStyle.SetLabelFont(132, "X")
kunoStyle.SetLabelSize(0.05, "xyz")
kunoStyle.SetTitleFont(132, "Y")
kunoStyle.SetTitleOffset(1.2, "xyz")
kunoStyle.SetTitleSize(0.05)
kunoStyle.SetLegendFillColor(0)
kunoStyle.SetLegendFont(132)
kunoStyle.SetLegendTextSize(0.04)
kunoStyle.SetStatColor(0)
kunoStyle.SetStatFont(132)
kunoStyle.SetStatFontSize(0.04)
kunoStyle.SetStatFormat("")

# Apply the custom style
ROOT.gROOT.SetStyle("kunoStyle")



# Additional canvas settings
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptDate(0)
ROOT.gStyle.SetLabelSize(0.03, "xyz")
ROOT.gStyle.SetTitleSize(0.035, "xyz")
ROOT.gStyle.SetTitleFont(22, "xyz")
ROOT.gStyle.SetLabelFont(22, "xyz")
ROOT.gStyle.SetTitleOffset(1.2, "y")
ROOT.gStyle.SetCanvasDefW(500)
ROOT.gStyle.SetCanvasDefH(500)
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetCanvasBorderSize(0)
ROOT.gStyle.SetPadLeftMargin(0.133)
ROOT.gStyle.SetPadRightMargin(0.1)
ROOT.gStyle.SetPadBottomMargin(0.1)
ROOT.gStyle.SetPadTopMargin(0.1)
ROOT.gStyle.SetPadLeftMargin(0.1)
ROOT.gStyle.SetPadRightMargin(0.1)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetPaperSize(20, 24)  # US letter size
'''

# Define the absolute path to the ROOT file
file_path = "../Matplotlib/Plots/histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the data histogram
data_hist = file.Get("data")

# Set up the canvas for drawing
canvas = ROOT.TCanvas("canvas", "Data Histogram with Confidence Limits", 800, 600)

# Adjust margins
canvas.SetMargin(0.15, 0.05, 0.15, 0.1)  # (left, right, bottom, top)

# Set colors for the histogram
data_hist.SetLineColor(ROOT.kBlue)

# Remove the statistics box
data_hist.SetStats(0)

# Draw the histogram
data_hist.Draw("HIST")

# Set titles for the axes
data_hist.GetXaxis().SetTitle("Mass")  # Replace with appropriate title
data_hist.GetYaxis().SetTitle("Counts")

# Create a Gaussian function
gauss = ROOT.TF1("gauss", "gaus", data_hist.GetXaxis().GetXmin(), data_hist.GetXaxis().GetXmax())

# Fit the Gaussian to the data histogram
data_hist.Fit(gauss, "S")

# Draw the fitted Gaussian on the histogram
gauss.SetLineColor(ROOT.kGreen)
gauss.Draw("SAME")

# Get fit parameters
mean = gauss.GetParameter(1)
sigma = gauss.GetParameter(2)

# Create parabolic confidence limits
def parabolic_shape(x, mean, sigma, scale):
    return scale * (1 - ((x - mean) ** 2) / (2 * sigma ** 2))

# Get the peak of the data histogram
peak_height = data_hist.GetMaximum()

# Create points for the parabola
x_values = np.linspace(mean - 2 * sigma, mean + 2 * sigma, 100)
y_68 = parabolic_shape(x_values, mean, sigma, peak_height * 0.6)  # 68% CL (±1σ)
y_95 = parabolic_shape(x_values, mean, sigma, peak_height * 0.4)  # 95% CL (±2σ)

# Create TGraph to draw the confidence levels
graph_68 = ROOT.TGraph(len(x_values), x_values, y_68)
graph_68.SetFillColorAlpha(ROOT.kMagenta, 0.3)  # Magenta for ±1σ
graph_68.SetLineColor(0)  # No border
graph_68.Draw("F SAME")

graph_95 = ROOT.TGraph(len(x_values), x_values, y_95)
graph_95.SetFillColorAlpha(ROOT.kOrange, 0.3)  # Orange for ±2σ
graph_95.SetLineColor(0)  # No border
graph_95.Draw("F SAME")

# Create a legend to show confidence limits
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(data_hist, "Data", "l")
legend.AddEntry(gauss, "Gaussian Fit", "l")
legend.AddEntry(graph_68, "68% CL (#pm1#sigma)", "f")
legend.AddEntry(graph_95, "95% CL (#pm2#sigma)", "f")
legend.Draw()

# Save the canvas as an image
canvas.SaveAs("Plots/Data_Histogram_with_Parabolic_Confidence_Limits.png")

# Close the ROOT file
file.Close()
