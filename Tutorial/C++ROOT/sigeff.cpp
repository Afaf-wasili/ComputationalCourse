#include "style.h"

void sigbkeff() {

    SetGlobalStyle();  // remove stat box, apply general style

    // Open ROOT file
    TFile *file = TFile::Open("mlpHiggs.root");

    // Get signal tree
    TTree *sig = (TTree*)file->Get("sig_filtered");

    // Total number of signal events
    int N = sig->GetEntries();

    // Variable from tree
    float acolin;
    sig->SetBranchAddress("acolin", &acolin);

    // Create graph for efficiency vs threshold
    TGraphErrors *g = new TGraphErrors();

    // Loop over acolinearity thresholds
    for (int t = 80; t <= 200; t++) {

        int count = 0;  // number of events passing the cut

        // Loop over all events
        for (int i = 0; i < N; i++) {
            sig->GetEntry(i);

            // Apply cut
            if (acolin >= t) count++;
        }

        // Efficiency = passed / total
        double eff = (double)count / N;

        // Binomial error
        double err = sqrt(eff * (1 - eff) / N);

        // Get current number of points in graph
        int p = g->GetN();

        // Add new point:
        // p = index (0,1,2,...)
        // t = x-axis (threshold)
        // eff = y-axis (efficiency)
        g->SetPoint(p, t, eff);

        // Set error for the same point:
        // x-error = 0 (no uncertainty on threshold)
        // y-error = efficiency error
        g->SetPointError(p, 0, err);
    }

    // Graph style
    g->SetTitle("Signal Efficiency;Acolinearity;Efficiency");
    g->SetLineColor(kBlue);
    g->SetMarkerStyle(20);

    // Canvas
    TCanvas *c = new TCanvas("c","",800,600);
    SetCanvasStyle(c);

    // Draw graph with axis, line, and points
    g->Draw("ALP");

    // Limit y-axis between 0 and 1
    g->GetYaxis()->SetRangeUser(0,1);

    // Save plot
    c->SaveAs("Signal_efficiency.png");
}
