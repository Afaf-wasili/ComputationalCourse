#include <TFile.h>
#include <TTree.h>
#include <TGraphErrors.h>
#include <TCanvas.h>
#include <TAxis.h>
#include <TStyle.h>
#include <TGaxis.h>
#include <TLegend.h>
#include <iostream>
#include <vector>



void SetupCustomStyle() {
    TStyle* customStyle = new TStyle("CustomStyle", "Custom Style for Plots");

    customStyle->SetCanvasColor(0);
    customStyle->SetPadColor(0);
    customStyle->SetFrameFillColor(0);
    customStyle->SetHistLineWidth(2);

    customStyle->SetLabelFont(132, "x");
    customStyle->SetLabelFont(132, "y");
    customStyle->SetLabelFont(132, "z");
    customStyle->SetLabelSize(0.04, "x");
    customStyle->SetLabelSize(0.04, "y");
    customStyle->SetLabelSize(0.04, "z");
    customStyle->SetTitleFont(130, "x");
    customStyle->SetTitleFont(130, "y");
    customStyle->SetTitleFont(130, "z");
    customStyle->SetTitleSize(0.05, "x");
    customStyle->SetTitleSize(0.05, "y");
    customStyle->SetTitleSize(0.05, "z");

    customStyle->SetLegendFont(132);
    customStyle->SetLegendTextSize(0.04);

    TGaxis::SetMaxDigits(3);
    TGaxis::SetExponentOffset(0.09, -0.09, "y");

    customStyle->SetPadGridX(true);
    customStyle->SetPadGridY(true);
    customStyle->SetGridWidth(1);
    customStyle->SetGridColor(kGray+2);
    customStyle->SetGridStyle(2);
    
    gROOT->SetStyle("CustomStyle");
    gStyle->cd();
    gStyle->SetPalette(84);
    gStyle->SetNumberContours(99);

    std::cout << "Custom style applied globally." << std::endl;
}

void scan_measuredC() {
  SetupCustomStyle();
  gStyle->SetOptStat(0);
    std::vector<double> misalignment_values;
    std::vector<double> p1_values;
    std::vector<double> p1_errors;

    std::string base_path = "/home/afafwasili/Datat_Muu/onebarlens";
    
    for (int i = 0; i < 100; i++) {
      //        double misalignment = i * 0.00009;
 double misalignment = i * 0.001;
      std::string filename = base_path + "/shiftx_" + std::to_string(i) + "/reco/tangle_3_30.00_0.0000_6.00.root";

        // Open ROOT file
        TFile *file = TFile::Open(filename.c_str(), "READ");
        if (!file || file->IsZombie()) {
            std::cerr << "Error: Cannot open " << filename << std::endl;
            continue;
        }

        // Get the correct canvas
        TCanvas *c1 = (TCanvas*)file->Get("tangle_3_30.00_0.0000_6.00");
        if (!c1) {
            std::cerr << "Error: TCanvas not found in " << filename << std::endl;
            file->Close();
            continue;
        }

        // Get histogram dynamically (first histogram in canvas)
        TH1F *hist = nullptr;
        for (auto obj : *(c1->GetListOfPrimitives())) {
            if (obj->InheritsFrom(TH1::Class())) {
                hist = (TH1F*)obj;
                break;
            }
        }

        if (!hist) {
            std::cerr << "Error: No histogram found in " << filename << std::endl;
            file->Close();
            continue;
        }

        // Ensure Gaussian fit function exists
        hist->Fit("gaus", "Q");  // Quiet mode
        TF1 *fit = hist->GetFunction("gaus");
        if (!fit) {
            std::cerr << "Error: Fit function 'gaus' not found in " << filename << std::endl;
            file->Close();
            continue;
        }

        // Extract p1 (resolution) and error
        double p1 = fit->GetParameter(2);  // 2: Sigma (resolution) , 1: mean
        double p1_err = fit->GetParError(2);

        // Store values
        misalignment_values.push_back(misalignment);
        p1_values.push_back(p1);
        p1_errors.push_back(p1_err);

        file->Close();
    }

    // Check if data was collected
    if (misalignment_values.empty()) {
        std::cerr << "No valid data found!" << std::endl;
        return;
    }

    // Create graph
    TCanvas *c1 = new TCanvas("c1", "p1 vs. Misalignment", 1200, 900);
    TGraphErrors *graph = new TGraphErrors(misalignment_values.size(), misalignment_values.data(), 
                                           p1_values.data(), nullptr, p1_errors.data());

    graph->SetMarkerStyle(29);
    graph->SetMarkerSize(1.5);
    graph->SetMarkerColor(kBlack);
    graph->SetLineWidth(1);
    graph->GetYaxis()->SetTitle("Measured #theta_{C} [rad]");
    //    graph->GetYaxis()->SetTitle("Resolution of #theta_{C} [rad]");
    graph->GetXaxis()->SetTitle("Misalignment Magnitude: Offset in x [mm]");

    graph->GetYaxis()->SetTitleOffset(1.8);
    graph->GetXaxis()->SetTitleOffset(1.0);
    graph->GetYaxis()->SetLabelSize(0.03);
    graph->GetXaxis()->SetLabelSize(0.03);
    graph->GetYaxis()->SetTitleFont(132);
    graph->GetXaxis()->SetTitleFont(132);
    graph->GetYaxis()->SetLabelFont(132);
    graph->GetXaxis()->SetLabelFont(132);
    graph->GetXaxis()->SetTitleSize(0.03);
    graph->GetYaxis()->SetTitleSize(0.03);
    //       graph->GetYaxis()->SetRangeUser(0.2,1);
      // Draw graph
    graph->GetXaxis()->SetRangeUser(0,0.1);
    c1->SetGridx();
    c1->SetGridy();
    graph->Draw("AP");

    // Legend
    TLegend *legend = new TLegend(0.43, 0.75, 0.85, 0.90);
    legend->SetBorderSize(0);
    legend->SetFillStyle(0);
    legend->SetTextSize(0.025);
    legend->SetTextFont(132);
    legend->AddEntry((TObject*)0, "DIRC at ePIC: Misalignment one bar with lens (Work in Progress)", "");
    legend->AddEntry((TObject*)0, "Particle ID: #pi/K", "");
    legend->AddEntry((TObject*)0, "Track Angle: #theta = 30 [deg]", "");
    legend->AddEntry((TObject*)0, "Momentum: 6 GeV/c", "");
    legend->Draw();

    // Save plot
    c1->SaveAs("p1_vs_misalignment.png");
    std::cout << "Plot saved as 'p1_vs_misalignment.png'" << std::endl;
}


