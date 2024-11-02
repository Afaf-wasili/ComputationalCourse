import ROOT

def plot_histograms():
    # Open the ROOT file and retrieve the histograms
    file = ROOT.TFile("sorted_mass.root")
    massPion = file.Get("histPion")
    massKaon = file.Get("histKaon")

    # Create a canvas with 3 pads
    canvas = ROOT.TCanvas("canvas", "Mass Distributions and Ratios", 800, 600)
    canvas.Divide(1, 3)  # 1 column, 3 rows

    # Pad 1: Draw massPion and massKaon histograms
    canvas.cd(1)
    massPion.SetLineColor(ROOT.kBlue)
    massPion.SetTitle("Mass Distributions")
    massPion.GetXaxis().SetTitle("Mass (GeV/c^2)")
    massPion.GetYaxis().SetTitle("Events")
    massPion.Draw()

    massKaon.SetLineColor(ROOT.kRed)
    massKaon.Draw("SAME")

    # Add legend
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(massPion, "Pion", "l")
    legend.AddEntry(massKaon, "Kaon", "l")
    legend.Draw()

    # Pad 2: Fit massPion with Gaussian and draw it
    canvas.cd(2)
    massPion.Fit("gaus")
    massPion.Draw()
    latex = ROOT.TLatex(0.1, 0.9, "Gaussian Fit of Pion Mass")
    latex.SetNDC()
    latex.Draw()

    # Pad 3: Calculate and draw the ratio
    canvas.cd(3)
    massRatio = massPion.Clone("massRatio")
    massRatio.Divide(massKaon)
    massRatio.SetTitle("Mass Ratio; Mass (GeV/c^2); Ratio")
    massRatio.GetYaxis().SetTitleOffset(1.5)
    massRatio.Draw()

    # Save the canvas to a file
    canvas.SaveAs("mass_plots.pdf")
    print("Canvas saved as 'mass_plots.pdf'.")

    # Close the ROOT file
    file.Close()

# Run the function
if __name__ == "__main__":
    plot_histograms()
