#include <iostream>
#include <TFile.h>
#include <TH1F.h>
#include <TRandom.h>

void createRootFile() {
    const int nEvents = 1000;
    const double meanPion = 0.13957; // Pion mass in GeV/c^2
    const double stdDevPion = 0.01;   // Standard deviation for pion

    const double meanKaon = 0.49367; // Kaon mass in GeV/c^2
    const double stdDevKaon = 0.02;   // Standard deviation for kaon

    // Create a ROOT file
    TFile file("sorted_mass.root", "RECREATE");

    // Create histograms for pions and kaons
    TH1F histPion("histPion", "Pion Mass Distribution; Mass (GeV/c^2); Events", 50, 0, 0.3);
    TH1F histKaon("histKaon", "Kaon Mass Distribution; Mass (GeV/c^2); Events", 50, 0, 1);

    // Generate random masses and fill histograms
    for (int i = 0; i < nEvents; ++i) {
        if (gRandom->Uniform() < 0.5) {
            // Generate a Gaussian-distributed random mass for pions
            double mass = gRandom->Gaus(meanPion, stdDevPion);
            histPion.Fill(mass);  // Fill pion histogram
        } else {
            // Generate a Gaussian-distributed random mass for kaons
            double mass = gRandom->Gaus(meanKaon, stdDevKaon);
            histKaon.Fill(mass);   // Fill kaon histogram
        }
    }

    // Write histograms to the ROOT file
    histPion.Write();
    histKaon.Write();
    file.Close();

    std::cout << "ROOT file 'sorted_mass.root' created with Gaussian-distributed histograms for pions and kaons." << std::endl;
}
