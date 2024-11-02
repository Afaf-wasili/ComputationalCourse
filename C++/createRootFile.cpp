#include <iostream>
#include <TFile.h>
#include <TH1F.h>
#include <TRandom.h>

void createRootFile() {
    const int nEvents = 100000;

    // Proton mass parameters
    const double meanProton = 0.93827; // Proton mass in GeV/c^2
    const double stdDevProton = 0.01;   // Standard deviation for proton

    const double meanKaon = 0.49367; // Kaon mass in GeV/c^2
    const double stdDevKaon = 0.02;   // Standard deviation for kaon

    // Create a ROOT file
    TFile file("sorted_mass.root", "RECREATE");

    // Create histograms for protons and kaons
    TH1F histProton("histProton", "Proton Mass Distribution; Mass (GeV/c^2); Events", 150, 0.8, 1.1);
    TH1F histKaon("histKaon", "Kaon Mass Distribution; Mass (GeV/c^2); Events", 150, 0, 1);

    // Generate random masses and fill histograms
    for (int i = 0; i < nEvents; ++i) {
        // Generate a Gaussian-distributed random mass for protons
        double mass = gRandom->Gaus(meanProton, stdDevProton);
        histProton.Fill(mass);  // Fill proton histogram

        // Generate a Gaussian-distributed random mass for kaons
        double massKaon = gRandom->Gaus(meanKaon, stdDevKaon);
        histKaon.Fill(massKaon);  // Fill kaon histogram
    }

    // Write histograms to the ROOT file
    histProton.Write();
    histKaon.Write();
    file.Close();

    std::cout << "ROOT file 'sorted_mass.root' created with Gaussian-distributed histograms for protons and kaons." << std::endl;
}
