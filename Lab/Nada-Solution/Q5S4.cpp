void Q5S4() {
    // Open the ROOT file
    TFile *file = TFile::Open("/Users/ndawyalmhzry/Master_project/ComputationalCourse/Tutorial/C++ROOT/mlpHiggs.root", "READ");
    
    TTree *sig_tree = (TTree *)file->Get("sig_filtered");

    int total_signal_events = sig_tree->GetEntries();

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

        // Loop through all events to count entries above the threshold
        for (int j = 0; j < total_signal_events; ++j) {
            sig_tree->GetEntry(j);
            if (acolin >= i) {
                ++signal_entry_count;
            }
        }

        // Define Efficiency "p"
        double p = static_cast<double>(signal_entry_count) / total_signal_events; // Efficiency
        double n = static_cast<double>(total_signal_events);  // Total events

	// Question 1: Define the Confidence Interval Calculation
        // Define the variables for the lower and upper bounds (confidence intervals) based on the equation:
        // Lower Bound = p - z * sqrt(p * (1 - p) / n)
        // Upper Bound = p + z * sqrt(p * (1 - p) / n)
	

        double sqrt_term = sqrt(p * (1 - p) / n);
        double lower_bound = p - z * sqrt_term;
        double upper_bound = p + z * sqrt_term;

        // Clamp bounds between 0 and 1
        lower_bound = (lower_bound < 0.0) ? 0.0 : lower_bound;
        upper_bound = (upper_bound > 1.0) ? 1.0 : upper_bound;

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

   
    TCanvas *canvas = new TCanvas("canvas", "Efficiency with Confidence Intervals", 800, 600);
    efficiency_graph->Draw("ALP");
    lower_bound_graph->Draw("LP SAME");
    upper_bound_graph->Draw("LP SAME");

    // Add legend
    TLegend *legend = new TLegend(0.6, 0.7, 0.9, 0.9, "nada");
    legend->AddEntry(efficiency_graph, "Efficiency", "LP");
    legend->AddEntry(lower_bound_graph, "Lower Bound (95%)", "L");
    legend->AddEntry(upper_bound_graph, "Upper Bound (95%)", "L");
    //  legend->Header("made by Nada");
    legend->Draw();

    // Save the canvas as a PNG file
    canvas->Update();
    canvas->SaveAs("EfficiencyWithConfidenceIntervals.png");

    // Close the file
    // file->Close();

    // std::cout << "Plot saved as EfficiencyWithConfidenceIntervals.png" << std::endl;
}
