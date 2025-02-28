#include <TFile.h>

#include <TCanvas.h>

#include <TH1F.h>

#include <TGraphErrors.h>

#include <TLegend.h>

#include <iostream>



void scan_residual() {

    // Define ROOT file base path

    std::string base_path = "/home/afafwasili/Datat_Muu/onebarlens";



    // Vectors to store misalignment values and std deviations

    std::vector<double> misalignment_values;  // X-axis

    std::vector<double> std_values;           // Y-axis (StdDev)

    std::vector<double> std_errors;           // Error bars



    for (int i = 0; i < 100; i++) {  

             double misalignment = i * 0.001; // X-axis misalignment

      //  double misalignment = i * 0.00009;



        // Construct the file path

  // std::string filename = base_path + "/shiftx_" + std::to_string(i) + "/reco/residual_3_30.00_0.0000_6.00.root";

std::string filename = base_path + "/shiftx_" + std::to_string(i) + "/reco/residual_3_30.00_0.0000_6.00.root";



        // Open ROOT file

        TFile *file = TFile::Open(filename.c_str(), "READ");

        if (!file || file->IsZombie()) {

            std::cerr << "Error: Cannot open " << filename << std::endl;

            continue;

        }



        // Get the TCanvas

        TCanvas *canvas = (TCanvas*)file->Get("residual_3_30.00_0.0000_6.00");

        if (!canvas) {

            std::cerr << "Error: Canvas not found in " << filename << std::endl;

            file->Close();

            continue;

        }



        // Extract the nameless TH1F histogram from the canvas

        TH1F *hist = (TH1F*)canvas->GetListOfPrimitives()->At(1);

        if (!hist) {

            std::cerr << "Error: Histogram not found in " << filename << std::endl;

            file->Close();

            continue;

        }



        // Get Standard Deviation (σ) and its error

	     	   double std_dev = hist->GetStdDev();

	       double std_dev_error = hist->GetStdDevError();

	//Get the mean

	//		double std_dev = hist->GetMean();

        //double std_dev_error = hist->GetMeanError();



	

        // Store values

        misalignment_values.push_back(misalignment);

        std_values.push_back(std_dev);

        std_errors.push_back(std_dev_error);



        // Close file

        file->Close();

    }



    // Check if data was collected

    if (misalignment_values.empty()) {

        std::cerr << "No valid data found!" << std::endl;

        return;

    }



    // Create a graph with error bars

    TCanvas *c1 = new TCanvas("c1", "Measured StdDev vs Misalignment", 1200, 900);

    TGraphErrors *graph = new TGraphErrors(misalignment_values.size(), misalignment_values.data(), 

                                           std_values.data(), nullptr, std_errors.data());



    graph->SetTitle("");

    graph->SetMarkerStyle(29);

    graph->SetMarkerSize(1.5);

    graph->SetMarkerColor(kBlack);

    graph->SetLineWidth(1);



    // Set axis labels

    //  graph->GetYaxis()->SetTitle("Measured Standard Deviation #sigma [rad]");

    //graph->GetXaxis()->SetTitle("Misalignment Magnitude: rot_z [rad]");



    graph->GetYaxis()->SetTitle("resolution of #theta_{C} residuals [rad]");

    //      graph->GetYaxis()->SetTitle(" #theta_{C} residuals [rad]");

      //graph->GetXaxis()->SetTitle("misalignment magnitude: offset in x [mm]");

      // graph->GetXaxis()->SetTitle("misalignment magnitude: rotation parallel about the beam axis [rad]");

    graph->GetXaxis()->SetTitle("Misalignment Magnitude: Offset in x [mm]");

     graph->GetYaxis()->SetTitleOffset(1.5);

    graph->GetXaxis()->SetTitleOffset(1.0);

    graph->GetYaxis()->SetLabelSize(0.03);

    graph->GetXaxis()->SetLabelSize(0.03);

    graph->GetYaxis()->SetTitleFont(132);

    graph->GetXaxis()->SetTitleFont(132);

    graph->GetYaxis()->SetLabelFont(132);

    graph->GetXaxis()->SetLabelFont(132);

    //graph->GetYaxis()->SetRangeUser(0, 0.23);

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

    legend->SetTextSize(0.023);

    legend->SetTextFont(132);

    //    legend->AddEntry((TObject*)0, "DIRC at ePIC: Misalignment only one bar (Work in Progress)", "");
legend->AddEntry((TObject*)0, "DIRC at ePIC: Misalignment only one bar with lens (Work in Progress)", "");

legend->AddEntry((TObject*)0, "Particle ID: #pi/K", "");

legend->AddEntry((TObject*)0, "Track Angle: #theta = 30 [deg]", "");

legend->AddEntry((TObject*)0, "Momentum: 6 GeV/c", "");

    legend->Draw();



			    

    // Save the plot

    c1->SaveAs("Plots/measured_std_vs_misalignment.png");

    std::cout << "Plot saved as 'measured_std_vs_misalignment.png'" << std::endl;

}
