void sigbkeff() {
    // Apply the modern style
    gROOT->SetStyle("ATLAS");
    gROOT->ForceStyle();

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

    // Open the ROOT file and get the signal tree
    TFile *file = TFile::Open("../mlpHiggs.root", "READ");
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

    // Get total number of signal events
    int total_signal_events = sig_tree->GetEntries();

    // Access the `acolin` variable from the tree
    float acolin;
    sig_tree->SetBranchAddress("acolin", &acolin);

    // Initialize graph for efficiency
    TGraphErrors *efficiency_graph = new TGraphErrors();

    // Loop over acolinearity thresholds
    for (int threshold = 80; threshold <= 200; ++threshold) {
        int signal_entry_count = 0; // Count valid signal entries for each threshold

        // Loop over signal entries
        for (int i = 0; i < total_signal_events; ++i) {
            sig_tree->GetEntry(i);

            // Count valid signal entries based on the acolinearity threshold
            if (acolin >= threshold) signal_entry_count++;
        }

        // Calculate efficiency
        double efficiency = static_cast<double>(signal_entry_count) / total_signal_events;
        double efficiency_error = std::sqrt(efficiency * (1 - efficiency) / total_signal_events);

        // Set points in the efficiency graph
        int n = efficiency_graph->GetN();
        efficiency_graph->SetPoint(n, threshold, efficiency);
        efficiency_graph->SetPointError(n, 0, efficiency_error);
    }

    // Configure graph appearance for efficiency
    efficiency_graph->SetTitle("Signal Efficiency vs Acolinearity");
    efficiency_graph->GetXaxis()->SetTitle("Acolinearity (degrees)");
    efficiency_graph->GetYaxis()->SetTitle("Signal Efficiency");
    efficiency_graph->SetLineColor(kBlue);
    efficiency_graph->SetMarkerStyle(20);
    efficiency_graph->SetMarkerColor(kBlue);

    // Draw the efficiency graph
    TCanvas *canvas = new TCanvas("canvas", "Signal Efficiency vs Acolinearity", 800, 600);
    canvas->SetGrid(); // Enable grid on the canvas
    efficiency_graph->Draw("ALP"); // Draw efficiency graph

    // Set Y-axis range from 0.0 to 1.0
    efficiency_graph->GetYaxis()->SetRangeUser(0.0, 1.0);

    //    canvas->Update();
    //gApplication->Run();

    // Close the file
    //    file->Close();
}
