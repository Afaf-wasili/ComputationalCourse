void fill2DHistogramsigbk() {
    // Open the ROOT file
    TFile *file = TFile::Open("mlpHiggs.root");
    if (!file || file->IsZombie()) {
        std::cerr << "Error: Could not open file mlpHiggs.root" << std::endl;
        return;
    }

    // Retrieve the trees
    TTree *sig_tree = (TTree*)file->Get("sig_filtered");
    TTree *bg_tree = (TTree*)file->Get("bg_filtered");
    if (!sig_tree || !bg_tree) {
        std::cerr << "Error: Could not retrieve one or both trees." << std::endl;
        file->Close();
        return;
    }

    // Variables to hold tree data
    Float_t bg_acolin = 0, sig_acolin = 0;
    bg_tree->SetBranchAddress("acolin", &bg_acolin);
    sig_tree->SetBranchAddress("acolin", &sig_acolin);

    // Create a 2D histogram
    TH2F *hist_2d = new TH2F("hist_2d", "Background vs Signal;Background;Signal",
                              100, 0, 200,  // Adjust X-axis range
                              100, 0, 200); // Adjust Y-axis range

    // Fill the histogram
    for (int j = 0; j < bg_tree->GetEntries(); ++j) {
        bg_tree->GetEntry(j);
        for (int i = 0; i < sig_tree->GetEntries(); ++i) {
            sig_tree->GetEntry(i);
            hist_2d->Fill(bg_acolin, sig_acolin);
        }
    }

    // Draw the histogram on the canvas
    TCanvas *c = new TCanvas("c", "Background vs Signal", 800, 600);
    hist_2d->Draw("COLZ");
    c->Show();

    // Clean up
    file->Close();
}
