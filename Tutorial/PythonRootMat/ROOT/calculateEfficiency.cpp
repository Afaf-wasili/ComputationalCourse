#include <iostream>
#include <ROOT/TFile.h>
#include <ROOT/TH1.h>
#include <ROOT/TCanvas.h>
#include <ROOT/TLegend.h>

void calculateEfficiency() {
    // Open the ROOT file
    TFile *file = TFile::Open("random_signal_background.root", "READ");

    // Retrieve the histograms for signal and background
    TH1F *signal_hist = dynamic_cast<TH1F*>(file->Get("histProton"));
    TH1F *background_hist = dynamic_cast<TH1F*>(file->Get("histKaon"));

    // Check if the histograms were retrieved correctly
    if (!signal_hist || !background_hist) {
        std::cerr << "Error: Histograms not found!" << std::endl;
        return;
    }

    // Calculate the total number of signal events and the number of detected signal events
    double total_signal_events = signal_hist->Integral(); // Total events in the signal histogram
    double detected_signal_events = signal_hist->GetBinContent(signal_hist->GetMaximumBin()); // Detected events (in the max bin)

    // Calculate efficiency
    double efficiency = (total_signal_events > 0) ? (detected_signal_events / total_signal_events) : 0;

    // Output the efficiency
    std::cout << "Total Signal Events: " << total_signal_events << std::endl;
    std::cout << "Detected Signal Events: " << detected_signal_events << std::endl;
    std::cout << "Efficiency: " << efficiency * 100 << "%" << std::endl;

    // Create a canvas for drawing
    TCanvas *canvas = new TCanvas("canvas", "Signal Efficiency", 800, 600);
    signal_hist->SetTitle("Signal Efficiency");
    signal_hist->GetXaxis()->SetTitle("Mass (GeV/c^2)");
    signal_hist->GetYaxis()->SetTitle("Events");
    signal_hist->Draw("HIST");

    // Draw efficiency as a line
    double efficiency_line = efficiency * total_signal_events; // Scale line for visualization
    TLine *line = new TLine(signal_hist->GetXaxis()->GetXmin(), efficiency_line, signal_hist->GetXaxis()->GetXmax(), efficiency_line);
    line->SetLineColor(kRed);
    line->SetLineStyle(2); // Dashed line
    line->Draw("SAME");

    // Add legend
    TLegend *legend = new TLegend(0.7, 0.7, 0.9, 0.9);
    legend->AddEntry(signal_hist, "Signal Histogram", "l");
    legend->AddEntry(line, "Efficiency Line", "l");
    legend->Draw();

    // Save the canvas as an image
    canvas->SaveAs("Plots/signal_efficiency.png");

    // Clean up
    delete canvas;
    file->Close();
}
