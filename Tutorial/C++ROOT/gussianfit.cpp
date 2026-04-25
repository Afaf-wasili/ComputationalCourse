#include "style.h"

void gussianfit() {
    // Apply global style
    SetGlobalStyle();

    // Open file
    TFile *file = TFile::Open("histo.root");

    // Get histogram
    TH1 *h = (TH1*)file->Get("data");

    // Create canvas with style
    TCanvas *c = new TCanvas("c", "Gaussian Fit", 800, 600);
    SetCanvasStyle(c);  // This enables grid and margins

    // Style histogram
    SetHistogramStyle(h);
    h->GetXaxis()->SetTitle("Mass (GeV/c^{2})");
    h->GetYaxis()->SetTitle("Counts");

    // Draw histogram
    h->Draw("HIST");


    //gussianfit
    TF1 *g =  new TF1("g","gaus",70,120); //70:begining y axis 120: ending y axis
    h->Fit(g,"");
    g->Draw("HIST SAME");

    //Extract fit parameters
    double mean = g->GetParameter(1);
    double sigma = g->GetParameter(2);
    double mean_err = g->GetParError(1);
    double sigma_err = g->GetParError(2);



    // Create legend with results
    TLegend *leg = CreateLegend();
    leg->AddEntry(h, "Data", "l");
    leg->AddEntry(g, "Gussian fit", "l");
    leg->AddEntry((TObject*)0, Form("#mu = %.3f  #pm %.3f", mean, mean_err),""); //mu : mean
     leg->AddEntry((TObject*)0, Form("sigma = %.3f  #pm %.3f", sigma, sigma_err),"");
    leg->Draw();


    // Save in multiple formats
    c->SaveAs("gaussian_fit.png");

}
