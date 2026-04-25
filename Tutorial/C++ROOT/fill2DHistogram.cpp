void fill2DHistogram(){
  //open
  TFile *file = TFile::Open("histo.root");
  // Get histogrames
  TH1D *data_hist = (TH1D*)file->Get("data");
  TH1D *mc_hist = (TH1D*)file->Get("MC");

  //define 2D
  TH2D *hist_2D = new TH2D("","", 100,70, 120, 100, 60, 120); //("","",#bin, min_x, max_x, #bin, min_y, max_y)
    hist_2D->GetXaxis()->SetTitle("Data");
    hist_2D->GetYaxis()->SetTitle("MC ");


  //looping: filling
  for (int i = 1; i<= 120; ++i)
    hist_2D->Fill(data_hist->GetBinCenter(i), mc_hist->GetBinCenter(i)); //fill(x:y)


   TCanvas *c = new TCanvas("","", 800,600);

   hist_2D->Draw("COLZ");
  c->SaveAs("Data_MC_2D_Histogram.png");

}
