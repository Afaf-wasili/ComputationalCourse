#include <iostream>
#include <random>
#include <ROOT/TFile.h>
#include <ROOT/TH1F.h>

void gen() {
    const int nEvents = 1000;                // Number of events
    const double meanSignal = 0.995;         // Mean of signal (Proton mass in GeV/c^2)
    const double stdDevSignal = 0.01;        // Standard deviation for signal

    const double meanBackground = 0.49367;    // Mean of background (Kaon mass in GeV/c^2)
    const double stdDevBackground = 0.02;     // Standard deviation for background

    // Create a ROOT file
    TFile file("random_signal_background.root", "RECREATE");

    // Create histograms for signal and background
    TH1F histSignal("histProton", "Proton Mass Distribution; Mass (GeV/c^2); Events", 50, 0, 1);
    TH1F histBackground("histKaon", "Kaon Mass Distribution; Mass (GeV/c^2); Events", 50, 0, 1);

    // Generate random signal masses and fill the signal histogram
    std::default_random_engine generator;
    std::normal_distribution<double> signalDistribution(meanSignal, stdDevSignal);
    
    for (int i = 0; i < nEvents; ++i) {
        double mass = signalDistribution(generator);
        histSignal.Fill(mass);
    }

    // Generate random background masses and fill the background histogram
    std::normal_distribution<double> backgroundDistribution(meanBackground, stdDevBackground);
    
    for (int i = 0; i < nEvents; ++i) {
        double mass = backgroundDistribution(generator);
        histBackground.Fill(mass);
    }

    // Write histograms to the ROOT file
    histSignal.Write();
    histBackground.Write();
    file.Close();

    std::cout << "ROOT file 'random_signal_background.root' created with random signal and background histograms." << std::endl;
}
