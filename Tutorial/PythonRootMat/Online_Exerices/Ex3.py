'''
remove the statistical box and add tittle for the x and y axis. Also, save the plot in a specific directory   

'''
import ROOT

def create2D():
# Open the ROOT file and retrieve histograms                                                                                           
    file = ROOT.TFile.Open("histo.root")


    data_hist = file.Get("data")
    mc_hist = file.Get("MC")
    #hist = ROOT.TH1F("","",nbin,min _x, max_x) for 1 D                                                                                    

    # Create a 2D histogram using binning from data_hist and mc_hist                                                                       
    nbins = data_hist.GetNbinsX()  # Assuming both histograms have the same number of bins                                                 
    hist_2d = ROOT.TH2D("", "",
                        nbins, data_hist.GetXaxis().GetXmin(), data_hist.GetXaxis().GetXmax(),
                        nbins, mc_hist.GetXaxis().GetXmin(), mc_hist.GetXaxis().GetXmax())

    # Loop over the bins and fill the 2D histogram using bin centers and bin contents                                                      
    for i in range(1, nbins + 1):
        data_value = data_hist.GetBinContent(i)
        mc_value = mc_hist.GetBinContent(i)

        # Use bin centers from data_hist (x-axis) and mc_hist (y-axis)                                                                     
        data_bin_center = data_hist.GetBinCenter(i)
        mc_bin_center   = mc_hist.GetBinCenter(i)

        hist_2d.Fill(data_hist.GetBinCenter(i), mc_hist.GetBinCenter(i) )
