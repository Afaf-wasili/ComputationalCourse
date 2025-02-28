#include <TFile.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TGraphErrors.h>
#include <TLegend.h>
#include <iostream>

void scan_photon() {
    // Define ROOT file base path
    std::string base_path = "/home/afafwasili/Datat_Muu/onebarlens";

    // Vectors to store misalignment values and number of detected photons
    std::vector<double> misalignment_values;  // X-axis (Misalignment)
    std::vector<double> photon_counts;        // Y-axis (Mean detected photons)
    std::vector<double> photon_errors;        // Error bars

    for (int i = 0; i < 100; i++) {  
      //     double misalignment = i * 0.00009;  // Adjust misalignment scaling
    double misalignment = i * 0.001;
        // Correct ROOT filename based on your image
        std::string filename = base_path + "/shiftx_" + std::to_string(i) + "/reco/nph_3_30.00_0.0000_6.00.root";

        // Open ROOT file
        TFile *file = TFile::Open(filename.c_str(), "READ");
        if (!file || file->IsZombie()) {
            std::cerr << "Error: Cannot open " << filename << std::endl;
            continue;
        }

        // Get the TCanvas
        TCanvas *canvas = (TCanvas*)file->Get("nph_3_30.00_0.0000_6.00");
        if (!canvas) {
            std::cerr << "Error: Canvas not found in " << filename << std::endl;
            file->Close();
            continue;
        }

        // Extract the histogram of detected photons (Index might need adjusting)
        TH1F *hist = (TH1F*)canvas->GetListOfPrimitives()->At(1);
        if (!hist) {
            std::cerr << "Error: Histogram not found in " << filename << std::endl;
            file->Close();
            continue;
        }

        // Get Mean Detected Photons and its error
             double mean_photons = hist->GetMean();
        double mean_error = hist->GetMeanError();
	//double std_dev = hist->GetStdDev();

	//double std_dev_error = hist->GetStdDevError();

        // Store values
         misalignment_values.push_back(misalignment);
	 photon_counts.push_back(mean_photons);
        photon_errors.push_back(mean_error);
        //photon_counts.push_back(std_dev_error);                                                                        
	//        photon_errors.push_back(std_dev_error);  
        // Close file
        file->Close();
    }

    // Check if data was collected
    if (misalignment_values.empty()) {
        std::cerr << "No valid data found!" << std::endl;
        return;
    }

    // Create a graph with error bars
    TCanvas *c1 = new TCanvas("c1", "Number of Detected Photons vs Misalignment", 1200, 900);
    TGraphErrors *graph = new TGraphErrors(misalignment_values.size(), misalignment_values.data(), 
                                           photon_counts.data(), nullptr, photon_errors.data());
   
    graph->SetMarkerStyle(29);
    graph->SetMarkerSize(1.5);
    graph->SetMarkerColor(kBlack);
    graph->SetLineWidth(1);

    // Set axis labels
    graph->GetYaxis()->SetTitle(" Detected Photons #");
    graph->GetXaxis()->SetTitle("Misalignment Magnitude: offset in x");
    graph->GetYaxis()->SetTitleOffset(1.5);
    graph->GetXaxis()->SetTitleOffset(1.0);
    graph->GetYaxis()->SetLabelSize(0.03);
    graph->GetXaxis()->SetLabelSize(0.03);
    graph->GetYaxis()->SetTitleFont(132);
    graph->GetXaxis()->SetTitleFont(132);
    graph->GetYaxis()->SetLabelFont(132);
    graph->GetXaxis()->SetLabelFont(132);
       graph->GetYaxis()->SetRangeUser(0, 200);  // Adjust range based on expected photon counts
    graph->GetXaxis()->SetTitleSize(0.03);
    graph->GetYaxis()->SetTitleSize(0.03);

    // Draw the graph
    c1->SetGridx();
    c1->SetGridy();
    graph->Draw("AP");

    // Legend                                                                                                      
    TLegend *legend = new TLegend(0.43, 0.75, 0.85, 0.90);
    legend->SetBorderSize(0);
    legend->SetFillStyle(0);
    legend->SetTextSize(0.025);
    legend->SetTextFont(132);
    legend->AddEntry((TObject*)0, "DIRC at ePIC: Misalignment only one bar with lens (Work in Progress)", "");
    legend->AddEntry((TObject*)0, "Particle ID: #pi/K", "");
    legend->AddEntry((TObject*)0, "Track Angle: #theta = 30 [deg]", "");
    legend->AddEntry((TObject*)0, "Momentum: 6 GeV/c", "");
    legend->Draw();

    // Save the plot
    c1->SaveAs("Plots/detected_photons_vs_misalignment.png");
    std::cout << "Plot saved as 'detected_photons_vs_misalignment.png'" << std::endl;
}
