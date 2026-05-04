#include "style.h"

void sigeffpurity() {

    SetGlobalStyle();

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
    // QUESTION (0):
    // Define three graphs using TGraphErrors:
    //   - g_eff  (efficiency)
    //   - g_pur  (purity)
    //   - g_prod (eff × purity)
    // =========================



    // =========================
    // LOOP OVER THRESHOLDS
    // =========================
    for (int t = 80; t <= 200; t++) {

        int count_sig = 0;
        int count_bg  = 0;

        // =========================
        // SIGNAL LOOP
        // =========================
        for (int i = 0; i < Ns; i++) {
            sig->GetEntry(i);
            if (sig_acolin >= t) count_sig++;
        }

        // =========================
        // BACKGROUND LOOP
        // =========================
        for (int i = 0; i < Nb; i++) {
            bg->GetEntry(i);
            if (bg_acolin >= t) count_bg++;
        }

        // =========================
        // QUESTION (1):
        // Define:
        //   efficiency 
        //   purity     
        //   product    
        // =========================



        // =========================
        // QUESTION (2):
        // Compute binomial errors for:
        //   efficiency
        //   purity
        // =========================



        // =========================
        // QUESTION (3):
        // Get index p from graph
        // =========================



        // =========================
        // QUESTION (4):
        // Fill ALL graphs with points and errors:
        //   g_eff  → (t, efficiency)
        //   g_pur  → (t, purity)
        //   g_prod → (t, product)
        // =========================

    }

    // =========================
    // STYLE (given)
    // =========================
    g_eff->SetLineColor(kBlue);
    g_eff->SetMarkerColor(kBlue);
    g_eff->SetMarkerStyle(20);

    g_pur->SetLineColor(kRed);
    g_pur->SetMarkerColor(kRed);
    g_pur->SetMarkerStyle(21);

    g_prod->SetLineColor(kGreen+2);
    g_prod->SetMarkerColor(kGreen+2);
    g_prod->SetMarkerStyle(22);

    g_eff->SetTitle("Efficiency, Purity, and Optimization;Acolinearity Cut;Value");

    // =========================
    // CANVAS
    // =========================
    TCanvas *c = new TCanvas("c","",800,600);
    SetCanvasStyle(c);

    // =========================
    // QUESTION (5):
    // Draw all graphs on same canvas
    // =========================



  

    // =========================
    // QUESTION (6):
    // Create legend:
    //   Efficiency
    //   Purity
    //   Efficiency × Purity
    // =========================



    // =========================
    // QUESTION (7):
    // Save plot as:
    //   "eff_purity_product.png"
    // =========================

}
