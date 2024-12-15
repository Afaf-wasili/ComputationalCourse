
//Question-2 (S(CLO 2.1))-10points:
/*
You are given a ROOT file with two trees: sig_filtered (signal events) and bg_filtered (background events). 
The goal is to calculate the purity for signal events as a function of the acollinearity threshold (acolin) 

Instructions:
1- Write a ROOT macro or C++ program to:
   - Loop over acollinearity thresholds from 80 to 200.
   - Calculate the purity as the efficiency is already given
   - Calculate the product between the efficiency and purity
   - Estimate the error on each varaibles
   - Plot:
       * Efficiency with purity and the product between them with markers.
       
2- Label the plot them on the same canvas:
   - X-axis: Acollinearity threshold (degrees).
   - Y-axis: Efficiency, Purity, Efficiency * Purity.
   - Include a legend for Efficiency, Purity, Efficiency * Purity.          
   - Save the plot
*/




#include <TFile.h>
#include <TTree.h>
#include <TGraphErrors.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <iostream>
#include <cmath>


void Q2(){
 // Set font for axis titles and labels                                                                                                                                               
    gStyle->SetLabelFont(22, "X");
    gStyle->SetLabelFont(22, "Y");
    gStyle->SetTitleFont(22, "X");
    gStyle->SetTitleFont(22, "Y");

    // Set size of axis titles and labels                                                                                                                                                
    gStyle->SetLabelSize(0.03, "X");
    gStyle->SetLabelSize(0.03, "Y");
    gStyle->SetTitleSize(0.04, "X");
    gStyle->SetTitleSize(0.04, "Y");
    gStyle->SetMarkerSize(0.5);


 TFile *file = TFile::Open("ParticlePhysics.root", "READ");
    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }
    TTree *sig_tree = dynamic_cast<TTree *>(file->Get("sig_filtered"));
    if (!sig_tree) {
        std::cerr << "Error: Signal tree not found!" << std::endl;
        file->Close();
        return;
    }
    int total_signal_events = sig_tree->GetEntries();
    float acolin;
    sig_tree->SetBranchAddress("acolin", &acolin);
    TGraphErrors *efficiency_graph = new TGraphErrors();
    for (int threshold = 80; threshold <= 200; ++threshold) {
        int signal_entry_count = 0; 
        for (int i = 0; i < total_signal_events; ++i) {
            sig_tree->GetEntry(i);
            if (acolin >= threshold) signal_entry_count++;
        }
	Title("Acolinearity (degrees)");
	efficiency_graph->GetYaxis()->SetTitle("Signal Efficiency");
	efficiency_graph->SetLineColor(kBlue);
	efficiency_graph->SetMarkerStyle(20);
	efficiency_graph->SetMarkerColor(kBlue);

	TCanvas *canvas = new TCanvas("canvas", "Signal Efficiency vs Acolinearity", 800, 600);
	canvas->SetGrid(); 
	efficiency_graph->Draw("ALP"); 

	efficiency_graph->GetYaxis()->SetRangeUser(0.0, 1.0);
  
        double efficiency = static_cast<double>(signal_entry_count) / total_signal_events;
        double efficiency_error = std::sqrt(efficiency * (1 - efficiency) / total_signal_events);

    
        int n = efficiency_graph->GetN();
        efficiency_graph->SetPoint(n, threshold, efficiency);
        efficiency_graph->SetPointError(n, 0, efficiency_error);
    }


    efficiency_graph->SetTitle("Signal Efficiency vs Acolinearity");
    efficiency_graph->GetXaxis()->SetTitle("Acolinearity (degrees)");
    efficiency_graph->GetYaxis()->SetTitle("Signal Efficiency");
    efficiency_graph->SetLineColor(kBlue);
    efficiency_graph->SetMarkerStyle(20);
    efficiency_graph->SetMarkerColor(kBlue);

    TCanvas *canvas = new TCanvas("canvas", "Signal Efficiency vs Acolinearity", 800, 600);
    canvas->SetGrid(); 
    efficiency_graph->Draw("ALP"); // Draw efficiency graph
    efficiency_graph->GetYaxis()->SetRangeUser(0.0, 1.0);

    //    canvas->Update();                                                                                                                                                                 //gApplication->Run();                                                                                                                                                                  // Close the file                                                                                                                                                                       //    file->Close();                                                                                                                                                                 
}

