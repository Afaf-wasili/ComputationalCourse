#include"style.h"

void sigbk(){
  SetGlobalStyle();

//tree, leave: bg_filtered, sig_filtered: acolin
  //open
  TFile *file = TFile::Open("mlpHiggs.root", "read");
 //Get Tree
  TTree *bg_tree =  (TTree*)file->Get("bg_filtered");
  TTree *sig_tree =  (TTree*)file->Get("sig_filtered");

  //Get histograms
  TH1F *bg_hist = new TH1F("", "",100, 30, 180); //("","", #bin, min_x,max_x)
  TH1F *sig_hist = new TH1F("", "",100, 30, 180);


  //variables to hold the values
  Float_t bg_acolin = 0;
  Float_t sig_acolin = 0;


  //set branch addresses
  bg_tree->SetBranchAddress("acolin", &bg_acolin);
  sig_tree->SetBranchAddress("acolin", &sig_acolin);

  //fill: first leave
   for (int i=0; i < sig_tree->GetEntries(); ++i){
    sig_tree->GetEntry(i);
    sig_hist->Fill(sig_acolin);
  }

   //fill: second leave

   for (int i=0; i < bg_tree->GetEntries(); ++i){
    bg_tree->GetEntry(i);
    bg_hist->Fill(bg_acolin);
  }

   //style
   bg_hist->GetXaxis()->SetTitle("mass");
   bg_hist->GetYaxis()->SetTitle("Number of Events");
  bg_hist->SetLineColor(kRed);  // Set background histogram color to red
  sig_hist->SetLineColor(kBlue);  // Set signal histogram color to blue




  TCanvas *c = new  TCanvas("","",800,900);


  bg_hist->Draw("HIST");
  sig_hist->Draw("HIST SAME");

    //legend
  TLegend *leg =  CreateLegend();
  leg->AddEntry(bg_hist ,"bg","l" ); //l: line
  leg->AddEntry(sig_hist ,"sig","l" ); //f: filling: box
  leg->Draw();


  c->SaveAs("Plots/sigkg.png");


