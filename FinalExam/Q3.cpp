//Question-3 S(CLO 2.2)-10points:
/*
Complete the following C++ script:
1. Adjust the Histogram Binning and Axis Ranges: Change the number of bins to 130
2. Set the axis ranges from 0 to 150
3. Draw the 2D-Histogram with the "COLZ" Option
4. Save the Canvas as a PNG File
*/

#include <TFile.h>
#include <TTree.h>
#include <TGraphErrors.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <iostream>
#include <cmath>

void Q3() {
  
    gStyle->SetLabelFont(22, "X");
    gStyle->SetLabelFont(22, "Y");
    gStyle->SetTitleFont(22, "X");
    gStyle->SetTitleFont(22, "Y");

    gStyle->SetLabelSize(0.03, "X");
    gStyle->SetLabelSize(0.03, "Y");
    gStyle->SetTitleSize(0.04, "X");
    gStyle->SetTitleSize(0.04, "Y");
    gStyle->SetMarkerSize(0.5);

   

    TFile *file = TFile::Open("ParticlePhysics.root");
    TTree *sig_tree = (TTree*)file->Get("sig_filtered");
    TTree *bg_tree = (TTree*)file->Get("bg_filtered");

    Float_t bg_minvis = 0, sig_minvis = 0;
    bg_tree->SetBranchAddress("minvis", &bg_minvis);
    sig_tree->SetBranchAddress("minvis", &sig_minvis);

 
    TH2F *hist_2d = new TH2F("hist_2d", "Background vs Signal;Background;Signal",
                              100, 0, 200,                                                                                                                       
                              100, 0, 200); 

    for (int j = 0; j < bg_tree->GetEntries(); ++j) {
        bg_tree->GetEntry(j);
        for (int i = 0; i < sig_tree->GetEntries(); ++i) {
            sig_tree->GetEntry(i);
            hist_2d->Fill(bg_minvis, sig_minvis);
        }
    }
    TCanvas *c = new TCanvas("c", "Background vs Signal", 800, 600);
 
}
