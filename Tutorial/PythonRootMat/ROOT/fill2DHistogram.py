import ROOT

def fill2DHistogram():

    # Open the ROOT file and retrieve histograms
    file = ROOT.TFile.Open("../Matplotlib/Plots/histo.root")


    data_hist = file.Get("data")
    mc_hist = file.Get("MC")


    # Create a 2D histogram using binning from data_hist and mc_hist
    nbins = data_hist.GetNbinsX()  # Assuming both histograms have the same number of bins
    hist_2d = ROOT.TH2F("hist_2d", "Data vs MC;Data;MC",
                        nbins, data_hist.GetXaxis().GetXmin(), data_hist.GetXaxis().GetXmax(),
                        nbins, mc_hist.GetXaxis().GetXmin(), mc_hist.GetXaxis().GetXmax())

    # Loop over the bins and fill the 2D histogram using bin centers and bin contents
    for i in range(1, nbins + 1):
        data_value = data_hist.GetBinContent(i)
        mc_value = mc_hist.GetBinContent(i)

        # Use bin centers from data_hist (x-axis) and mc_hist (y-axis)
        data_bin_center = data_hist.GetBinCenter(i)
        mc_bin_center = mc_hist.GetBinCenter(i)

        # Fill the 2D histogram using bin centers, weighted by data_value
        hist_2d.Fill(data_bin_center, mc_bin_center, data_value)

    # Draw and save the 2D histogram
    c = ROOT.TCanvas("c", "Data vs MC", 800, 600)
    hist_2d.Draw("COLZ")
    c.SaveAs("Plots/Data_MC_2D_Histogram.png")

    # Close the ROOT file
    file.Close()

# Run the function
fill2DHistogram()
