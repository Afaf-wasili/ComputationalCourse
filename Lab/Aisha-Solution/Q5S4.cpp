void Q5S4() {
    TFile *file = TFile::Open("mlpHiggs.root", "READ");
    
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
        // Define lower and upper bounds based on the formula above
        double lower_bound = p - z * sqrt(p * (1 - p) / n);
          double upper_bound = p + z * sqrt(p * (1 - p) / n);
        // Add points to graphs

	  
    

	  
        int point_index = efficiency_graph->GetN();
        efficiency_graph->SetPoint(point_index, i, p);                      // Set point for efficiency graph
        lower_bound_graph->SetPoint(point_index, i, lower_bound);           // Set point for lower bound graph
        upper_bound_graph->SetPoint(point_index, i, upper_bound);           // Set point for upper bound graph
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

    // Question 2: Add legend                                                                                                                                                             
    TLegend *legend = new TLegend(0.6, 0.7, 0.9, 0.9);
    legend->SetHeader("AISHAH");
    legend->AddEntry(efficiency_graph,"efficiency","l");
    legend->AddEntry(lower_bound_graph,"lower_bound","l");
    legend->AddEntry(upper_bound_graph,"upper_bound","l");
    legend->Draw();
     canvas->Update();
    canvas->SaveAs("EfficiencyWithConfidenceIntervals.png");

    canvas->Show();
      //file->Close();
    
    
}
