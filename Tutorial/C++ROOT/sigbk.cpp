void sigbk(){
gROOT-> SetStyle("ATLAS");
//gROOT->ForceStyle();

  TFile *file = TFile::Open("mlpHiggs.root", "read");
  TTree *bg_tree =  (TTree*)file->Get("bg_filtered");
  TTree *sig_tree =  (TTree*)file->Get("sig_filtered");


  TH1F *bg_hist = new TH1F("bg_acolin", "Acollinearity - Background",50, 30, 180);
  TH1F *sig_hist = new TH1F("sig_acolin", "Acollinearity - Signal", 50, 30, 180);

  //  bg_tree->Draw("acolin >> bg_acolin ");
  //sig_tree->Draw("acolin >> sig_acolin");
  //variables to hold the values
  Float_t bg_acolin = 0;
  Float_t sig_acolin = 0; 

  
  //set branch addresses
  bg_tree->SetBranchAddress("acolin", &bg_acolin);
  sig_tree->SetBranchAddress("acolin", &sig_acolin);

  //fill
  for (int i=0; i < sig_tree->GetEntries(); ++i){
    sig_tree->GetEntry(i);
    sig_hist->Fill(sig_acolin);
  }



   for (int i=0; i < bg_tree->GetEntries(); ++i){
    bg_tree->GetEntry(i);
    bg_hist->Fill(bg_acolin);
  }

  bg_hist->SetXTitle("mass");
  bg_hist->SetYTitle("Number of Events");
  bg_hist->SetLineColor(kRed);  // Set background histogram color to red
  sig_hist->SetLineColor(kBlue);  // Set signal histogram color to blue                         



  TCanvas *c = new  TCanvas("","",800,900);
  bg_hist->Draw("HIST");
  sig_hist->Draw("HIST SAME");
  c->Show();
  //c->SaveAs("Plots/sigkg.png");  


}
