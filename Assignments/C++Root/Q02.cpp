#include "style.h"

void fill2DHistogramsigbk() {

    SetGlobalStyle();  // apply ROOT style

    // Open ROOT file
    TFile *file = TFile::Open("mlpHiggs.root");

    // =========================
    // Question 1:
    // How do you access the signal tree "sig_filtered" and the background tree "bg_filtered"?
   


    // Variables from tree branches
    float sig_acolin = 0;
    float bg_acolin  = 0;

    // =========================
    // Question 2:
 
    // Use SetBranchAddress for both trees.
    // =========================


    // =========================
    // Question 3:
    // How do you create a 2D histogram named "h2" with:
    // - X-axis: Background (0 → 200, 100 bins)
    // - Y-axis: Signal (0 → 200, 100 bins)?
    // =========================


    // Loop over background events
    for (int i = 0; i < bg->GetEntries(); i++) {

        bg->GetEntry(i);  // get one background event

        // =========================
        // Question 4:
        // How do you create a loop over all signal events inside this loop?
        // =========================


        // =========================
        // Question 5:
        // Inside the signal loop:
        // - How do you read each signal event?
        // - How do you fill the histogram using (bg_acolin, sig_acolin)?
        // =========================

    } // end background loop


    // Canvas
    TCanvas *c = new TCanvas("c", "Sig vs Bkg", 800, 600);
    SetCanvasStyle(c);

    // =========================
    // Question 6:
    // How do you draw the histogram as 2D?
    // =========================


    // =========================
    // Question 7:
    // How do you save the canvas as an image file named "Sig_vs_Bkg_2D.png"?
    // =========================


    // Close file
    file->Close();
}
