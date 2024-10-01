import ROOT

def fill2DHistogram():
    ROOT.gStyle.SetPalette(ROOT.kRainBow)
    # Open the ROOT file and retrieve histograms                                                                                           
    file = ROOT.TFile.Open("histo.root")


    data_hist = file.Get("data")
    mc_hist = file.Get("MC")
    #hist = ROOT.TH1F("","",nbin,min _x, max_x) for 1 D                                                                                    

    # Create a 2D histogram using binning from data_hist and mc_hist                                                                       
    nbins = data_hist.GetNbinsX()  # Assuming both histograms have the same number of bins                                                 
    hist_2d = ROOT.TH2D("hist_2d", "Data vs MC;Data;MC",nbins, 70, 120, nbins, 70, 120)

    # Loop over the bins and fill the 2D histogram using bin centers and bin contents                                                      
    for i in range(1, nbins + 1):
        data_value = data_hist.GetBinContent(i)
        mc_value = mc_hist.GetBinContent(i)

 
        hist_2d.Fill(data_hist.GetBinContent(i), mc_hist.GetBinContent(i))

      # Draw and save the 2D histogram                                                                                                      
    c = ROOT.TCanvas("c", "Data vs MC", 800, 600)
    hist_2d.Draw("colz")
    c.Show()
    #c.SaveAs("Plots/Data_MC_2D_Histogram.png")                                                                                            

    # Close the ROOT file                                                                                                                  
    #file.Close()                                                                                                                           #to keep GUI running and close it mannually
    ROOT.gApplication.Run()
# Run the function                                                                                                                         
fill2DHistogram()


