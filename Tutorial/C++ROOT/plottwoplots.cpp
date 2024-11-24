void plottwoplots(){

gROOT-> SetStyle("ATLAS");
gROOT->ForceStyle();

  // Set font for axis titles and labels                                                     

  TFile* file = TFile::Open("histo.root","READ"); 
  TH1* data_hist = (TH1*)file->Get("data");
  TH1* mc_hist = (TH1*)file->Get("MC");

  TCanvas* canvas = new TCanvas("","", 800, 600);
  //  canvas->SetMargin(0.15, 0.05, 0.15, 0.1);
  data_hist->SetMarkerColor(kBlue);
  mc_hist->SetMarkerColor(kRed);

  data_hist->SetStats(0);
  mc_hist->SetStats(0);

  data_hist->Draw("P");
  mc_hist->Draw("P SAME");


  data_hist->GetXaxis()->SetTitle("Mass");  
  data_hist->GetYaxis()->SetTitle("Counts");
  data_hist->SetTitle("MC and data");

  TLegend* legend = new TLegend(0.5, 0.5, 0.7, 0.7);
  legend->SetHeader("made by Afaf");
  legend->AddEntry(data_hist, "Data", "P");
  legend->AddEntry(mc_hist, "MC", "P");
  legend->Draw();


  canvas->SaveAs("Plots/Data_MC_Histograms.png");

}
