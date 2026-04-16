
#include "style.h"

//histo.root
// data, MC

void plottwoplots(){
  SetGlobalStyle();


  //open file
  TFile *file = TFile::Open("histo.root");


  //Get histograms
  TH1 *data = (TH1*)file->Get("data");
  TH1 *mc = (TH1*)file->Get("MC");

  SetHistogramStyle(data);

  //canvas
  TCanvas *c = new TCanvas("","",800,600);
  SetCanvasStyle(c);

  //title x , y
  data->GetXaxis()->SetTitle("Mass (GeV/c)");
  data->GetYaxis()->SetTitle("Events");



  //Draw
  data->Draw("HIST");
  mc->Draw("HIST SAME");


  //legend
  TLegend *leg =  CreateLegend();
  leg->AddEntry(data,"Data-plot","l" ); //l: line
  leg->AddEntry(mc,"MC-plot","f" ); //f: filling: box
  leg->Draw();



  //Save
  c->SaveAs("plots/Data_MC.png");
