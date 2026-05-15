#include "style.h"

void sigeffpurity() {

    SetGlobalStyle();  // remove stat box, apply general style

    // =========================
    // OPEN FILE
    // =========================
    TFile *file = TFile::Open("mlpHiggs.root");

    // =========================
    // GET TREES
    // =========================
    TTree *sig = (TTree*)file->Get("sig_filtered");
    TTree *bg  = (TTree*)file->Get("bg_filtered");

    // =========================
    // TOTAL EVENTS
    // =========================
    int Ns = sig->GetEntries();
    int Nb = bg->GetEntries();

    // =========================
    // VARIABLE
    // =========================
    float sig_acolin, bg_acolin;

    sig->SetBranchAddress("acolin", &sig_acolin);
    bg->SetBranchAddress("acolin", &bg_acolin);

    // =========================
    // GRAPHS
    // =========================
    TGraphErrors *g_eff  = new TGraphErrors();
    TGraphErrors *g_pur  = new TGraphErrors();
    TGraphErrors *g_prod = new TGraphErrors();

    // =========================
    // LOOP OVER THRESHOLDS
    // =========================
    for (int t = 80; t <= 200; t++) {

        int count_sig = 0;
        int count_bg  = 0;

        // =========================
        // SIGNAL LOOP (EFFICIENCY)
        // =========================
        for (int i = 0; i < Ns; i++) {
            sig->GetEntry(i);
            if (sig_acolin >= t) count_sig++;
        }

        double eff = (double)count_sig / Ns;
        double err = sqrt(eff * (1 - eff) / Ns);

        int p = g_eff->GetN();
        g_eff->SetPoint(p, t, eff);
        g_eff->SetPointError(p, 0, err);

        // =========================
        // BACKGROUND LOOP
        // =========================
        for (int i = 0; i < Nb; i++) {
            bg->GetEntry(i);
            if (bg_acolin >= t) count_bg++;
        }

        // =========================
        // PURITY
        // =========================
        double purity = 0;
        if ((count_sig + count_bg) > 0)
            purity = (double)count_sig / (count_sig + count_bg);

        int p2 = g_pur->GetN();
        g_pur->SetPoint(p2, t, purity);

        // =========================
        // PRODUCT (EFF × PURITY)
        // =========================
        double product = eff * purity;

        int p3 = g_prod->GetN();
        g_prod->SetPoint(p3, t, product);
    }

    // =========================
    // STYLE (FIXED COLORS + ERROR BARS)
    // =========================

    // Efficiency
    g_eff->SetLineColor(kBlue);
    g_eff->SetMarkerColor(kBlue);
    g_eff->SetMarkerStyle(20);
    g_eff->SetMarkerSize(1.0);
    g_eff->SetLineWidth(2);

    // Purity
    g_pur->SetLineColor(kRed);
    g_pur->SetMarkerColor(kRed);
    g_pur->SetMarkerStyle(21);
    g_pur->SetMarkerSize(1.0);
    g_pur->SetLineWidth(2);

    // Product
    g_prod->SetLineColor(kGreen+2);
    g_prod->SetMarkerColor(kGreen+2);
    g_prod->SetMarkerStyle(22);
    g_prod->SetMarkerSize(1.0);
    g_prod->SetLineWidth(2);

    // Title
    g_eff->SetTitle("Efficiency, Purity, and Optimization;Acolinearity Cut;Value");

    // =========================
    // CANVAS
    // =========================
    TCanvas *c = new TCanvas("c","",800,600);
    SetCanvasStyle(c);

    g_eff->Draw("ALP");        // efficiency with error bars
    g_pur->Draw("LP SAME");
    g_prod->Draw("LP SAME");

    g_eff->GetYaxis()->SetRangeUser(0,1);

    // =========================
    // LEGEND
    // =========================
    TLegend *leg = new TLegend(0.65,0.70,0.88,0.88);
    leg->AddEntry(g_eff,"Efficiency","l");
    leg->AddEntry(g_pur,"Purity","l");
    leg->AddEntry(g_prod,"Efficiency × Purity","l");
    leg->Draw();

    // =========================
    // SAVE OUTPUT
    // =========================

    // =========================
    // SAVE OUTPUT
    // =========================
    c->SaveAs("eff_purity_product.png");
}
