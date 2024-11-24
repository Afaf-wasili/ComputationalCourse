#include <TFile.h>
#include <TTree.h>
#include <TGraphErrors.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <iostream>
#include <cmath>

void test() {
    TFile *file = TFile::Open("mlpHiggs.root", "READ");
    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file" << std::endl;
        return;
    }

    TTree *sig_tree = (TTree *)file->Get("sig_filtered");
    if (!sig_tree) {
        std::cerr << "Error: sig_filtered tree not found" << std::endl;
        return;
    }

    int total_signal_events = sig_tree->GetEntries();
    if (total_signal_events == 0) {
        std::cerr << "Error: No signal events found" << std::endl;
        return;
    }

    // Define variables
    Float_t acolin;
    sig_tree->SetBranchAddress("acolin", &acolin);

    // Confidence level (95%)
    double z = 1.96;

    // Graphs for efficiency and confidence bounds
    TGraphErrors *efficiency_graph = new TGraphErrors();
    TGraphErrors *lower_bound_graph = new TGraphErrors();
    TGraphErrors *upper_bound_graph = new TGraphErrors();

    // Loop over thresholds
    for (int i = 80; i < 200; ++i) {
        int signal_entry_count = 0;

        // Count valid signal entries
        for (int j = 0; j < total_signal_events; ++j) {
            sig_tree->GetEntry(j);
            if (acolin >= i) {
                ++signal_entry_count;
            }
        }

        double p = static_cast<double>(signal_entry_count) / total_signal_events; // Efficiency
        double n = static_cast<double>(total_signal_events);

        // Wald Confidence Interval
        double lower_bound = p - z * sqrt(p * (1 - p) / n);
        double upper_bound = p + z * sqrt(p * (1 - p) / n);

        // Add points to graphs
        int point_index = efficiency_graph->GetN();
        efficiency_graph->SetPoint(point_index, i, p);
        lower_bound_graph->SetPoint(point_index, i, lower_bound);
        upper_bound_graph->SetPoint(point_index, i, upper_bound);
    }

    // Configure graph styles
    efficiency_graph->SetTitle("Efficiency with 95% Confidence Intervals");
    efficiency_graph->GetXaxis()->SetTitle("Acolinearity Threshold");
    efficiency_graph->GetYaxis()->SetTitle("Efficiency");
    efficiency_graph->SetLineColor(kBlue);
    efficiency_graph->SetMarkerStyle(20);
    efficiency_graph->SetMarkerColor(kBlue);

    lower_bound_graph->SetLineColor(kRed);
    lower_bound_graph->SetLineStyle(2);

    upper_bound_graph->SetLineColor(kGreen + 2);
    upper_bound_graph->SetLineStyle(2);

    // Draw on canvas
    TCanvas *canvas = new TCanvas("canvas", "Efficiency with Confidence Intervals", 800, 600);
    efficiency_graph->Draw("ALP");
    lower_bound_graph->Draw("LP SAME");
    upper_bound_graph->Draw("LP SAME");

    // Add legend
    TLegend *legend = new TLegend(0.6, 0.7, 0.9, 0.9);
    legend->AddEntry(efficiency_graph, "Efficiency", "lp");
    legend->AddEntry(lower_bound_graph, "Lower Bound (95% CL)", "lp");
    legend->AddEntry(upper_bound_graph, "Upper Bound (95% CL)", "lp");
    legend->Draw();

    canvas->Update();
    canvas->SaveAs("EfficiencyWithConfidenceIntervals.png");

    file->Close();
}
