#include <iostream>
#include "TFile.h"
#include "TH1.h"
#include "TRandom.h"

int main() {
    // Create a ROOT file to store histograms
    TFile *file = new TFile("histograms.root", "RECREATE");

    // Create a 1D histogram
    TH1F *histogram = new TH1F("histogram", "Example Histogram", 100, -3, 3);

    // Fill histogram with random numbers
    TRandom random;
    for (int i = 0; i < 10000; ++i) {
        histogram->Fill(random.Gaus(0, 1)); // Gaussian distribution with mean 0, sigma 1
    }

    // Write histogram to the ROOT file
    histogram->Write();

    // Close the file
    file->Close();

    // Clean up
    delete file;

    std::cout << "Histogram saved to histograms.root" << std::endl;

    return 0;
}
