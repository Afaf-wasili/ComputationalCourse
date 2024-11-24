void fill2DHistogram(){

  TFile *file = TFile::Open("histo.root");
  TH1D *data_hist = (TH1D*)file->Get("data");
  TH1D *mc_hist = (TH1D*)file->Get("MC");
  TH2D *hist_2d = new TH2D("","Data vs MC;Data;MC", 100, 70,120,100,70,120);


  for (int i=1; i <=100; ++i)
     hist_2d->Fill(data_hist->GetBinCenter(i), mc_hist->GetBinCenter(i));
  //TCanvas *c = new TCanvas("","", 800,600);
  hist_2d->Draw("COLZ");
  //c->Show(); 
  //c->SaveAs("Plots//Data_MC_2D_Histogram.png"); 

}
