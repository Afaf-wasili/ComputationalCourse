import ROOT

# Define the path to the ROOT file
file_path = "../Matplotlib/Plots/histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms
signal_hist = file.Get("data")  # Signal histogram
background_hist = file.Get("MC")  # Background histogram

# Create new histograms for efficiency, purity, product, and suppression factor
efficiency_hist = signal_hist.Clone("efficiency")
purity_hist = signal_hist.Clone("purity")
product_hist = signal_hist.Clone("product")
suppression_factor_hist = signal_hist.Clone("suppression_factor")

# Calculate efficiency, purity, suppression factor, and product
for bin in range(1, signal_hist.GetNbinsX() + 1):
    signal_count = signal_hist.GetBinContent(bin)
    background_count = background_hist.GetBinContent(bin)
    
    # Efficiency
    efficiency = (signal_count / background_count * 100) if background_count > 0 else 0
    efficiency_hist.SetBinContent(bin, efficiency)

    # Purity
    total_count = signal_count + background_count
    purity = (signal_count / total_count * 100) if total_count > 0 else 0
    purity_hist.SetBinContent(bin, purity)

    # Product of efficiency and purity
    product = (efficiency * purity / 100)  # Product as a fraction
    product_hist.SetBinContent(bin, product)

    # Suppression Factor (as a percentage)
    suppression_factor = (background_count / signal_count * 100) if signal_count > 0 else 0
    suppression_factor_hist.SetBinContent(bin, suppression_factor)

# Set up the canvas for drawing
canvas = ROOT.TCanvas("canvas", "Metrics: Efficiency, Purity, Product, Suppression Factor", 800, 600)

# Set logarithmic scale for Y-axis
canvas.SetLogy()

# Draw efficiency histogram
efficiency_hist.SetLineColor(ROOT.kGreen)
efficiency_hist.SetTitle("Efficiency, Purity, Product, and Suppression Factor (Log Scale)")
efficiency_hist.GetYaxis().SetTitle("Percentage")
efficiency_hist.GetXaxis().SetTitle("Bins")
efficiency_hist.Draw("HIST")

# Draw purity histogram
purity_hist.SetLineColor(ROOT.kBlue)
purity_hist.Draw("HIST SAME")

# Draw product histogram
product_hist.SetLineColor(ROOT.kMagenta)
product_hist.Draw("HIST SAME")

# Create a new graph for suppression factor
suppress_graph = ROOT.TGraph()
for bin in range(1, suppression_factor_hist.GetNbinsX() + 1):
    suppress_graph.SetPoint(bin - 1, efficiency_hist.GetBinCenter(bin), suppression_factor_hist.GetBinContent(bin))

# Set graph attributes
suppress_graph.SetLineColor(ROOT.kRed)
suppress_graph.SetMarkerStyle(20)
suppress_graph.SetMarkerColor(ROOT.kRed)

# Set the Y-axis limits to ensure the suppression factor is visible
max_value = max(efficiency_hist.GetMaximum(), purity_hist.GetMaximum(), product_hist.GetMaximum(), suppression_factor_hist.GetMaximum() * 100)
y2 = efficiency_hist.GetYaxis().Clone("y2")
y2.SetRangeUser(1, max_value * 1.5)  # Add some margin

# Draw the suppression factor graph
suppress_graph.Draw("P SAME")

# Set the secondary axis
canvas.Modified()
canvas.Update()
y2.SetTitleOffset(1.3)
y2.Draw("SAME")

# Create and draw the legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(efficiency_hist, "Efficiency (%)", "l")
legend.AddEntry(purity_hist, "Purity (%)", "l")
legend.AddEntry(product_hist, "Efficiency * Purity (%)", "l")
legend.AddEntry(suppress_graph, "Suppression Factor (%)", "p")
legend.Draw()

# Save the canvas as an image
canvas.SaveAs("Plots/Efficiency_Purity_Product_Suppression_Factor_Log.png")

# Close the ROOT file
file.Close()
