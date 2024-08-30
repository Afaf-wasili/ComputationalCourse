#include <TFile.h>
#include <TTree.h>
#include <TSystem.h>
#include <iostream>
#include <fstream>
#include <vector>

// Function to write an event to the LHE file
void WriteEvent(std::ofstream& lheFile, int numParticles, const std::vector<int>& pdgIds,
                const std::vector<int>& statuses, const std::vector<double>& px,
                const std::vector<double>& py, const std::vector<double>& pz,
                const std::vector<double>& energy, const std::vector<double>& mass) {
    lheFile << "<event>\n";
    lheFile << numParticles << " " << "0.0 0.0 0.0 0.0 0.0\n"; // Dummy values for weights and scales
    for (int i = 0; i < numParticles; ++i) {
        lheFile << pdgIds[i] << " "     // Particle ID
                << statuses[i] << " "   // Status
                << "0 0 "               // Mother particles (dummy)
                << "0 0 "               // Color flow (dummy)
                << px[i] << " "         // px
                << py[i] << " "         // py
                << pz[i] << " "         // pz
                << energy[i] << " "     // Energy
                << mass[i] << " "       // Mass
                << "0.0 0.0\n";         // Vertex information (dummy)
    }
    lheFile << "</event>\n";
}

// Function to convert a ROOT file to an LHE file
void ConvertRootToLHE(const char* rootFileName, const char* lheFileName) {
    TFile *file = TFile::Open(rootFileName);
    if (!file || file->IsZombie()) {
        std::cerr << "Error: Could not open the ROOT file!" << std::endl;
        return;
    }

    TTree *sig_filtered = (TTree*)file->Get("sig_filtered");
    TTree *bg_filtered = (TTree*)file->Get("bg_filtered");

    if (!sig_filtered || !bg_filtered) {
        std::cerr << "Error: Could not find the TTrees!" << std::endl;
        file->Close();
        return;
    }

    Float_t ptsumf, qelep, nch, msumf, minvis, acopl, acolin;
    sig_filtered->SetBranchAddress("ptsumf", &ptsumf);
    sig_filtered->SetBranchAddress("qelep",  &qelep);
    sig_filtered->SetBranchAddress("nch",    &nch);
    sig_filtered->SetBranchAddress("msumf",  &msumf);
    sig_filtered->SetBranchAddress("minvis", &minvis);
    sig_filtered->SetBranchAddress("acopl",  &acopl);
    sig_filtered->SetBranchAddress("acolin", &acolin);

    bg_filtered->SetBranchAddress("ptsumf", &ptsumf);
    bg_filtered->SetBranchAddress("qelep",  &qelep);
    bg_filtered->SetBranchAddress("nch",    &nch);
    bg_filtered->SetBranchAddress("msumf",  &msumf);
    bg_filtered->SetBranchAddress("minvis", &minvis);
    bg_filtered->SetBranchAddress("acopl",  &acopl);
    bg_filtered->SetBranchAddress("acolin", &acolin);

    std::ofstream lheFile(lheFileName);
    if (!lheFile.is_open()) {
        std::cerr << "Error: Could not open the LHE file for writing!" << std::endl;
        file->Close();
        return;
    }

    lheFile << "<LesHouchesEvents version=\"1.0\">\n";
    lheFile << "<header>\n";
    lheFile << "<!-- Header information -->\n";
    lheFile << "</header>\n";
    lheFile << "<init>\n";
    lheFile << "2212 2212 6500.0 6500.0 0 0\n"; // Example initial state
    lheFile << "1 1\n"; // Number of processes
    lheFile << "1 1.0 1.0 0 0 0\n"; // Process info (example)
    lheFile << "</init>\n";

    std::vector<int> pdgIds(1, 25); // PDG ID for Higgs (example)
    std::vector<int> statuses(1, 1); // Status (final state)
    std::vector<double> px(1), py(1), pz(1), energy(1), mass(1, 125.0); // Example values

    int numSigEvents = sig_filtered->GetEntries();
    for (int i = 0; i < numSigEvents; ++i) {
        sig_filtered->GetEntry(i);
        // Example: Set momentum and energy based on the variables
        px[0] = ptsumf; py[0] = 0; pz[0] = 0; energy[0] = msumf;
        WriteEvent(lheFile, 1, pdgIds, statuses, px, py, pz, energy, mass);
    }

    pdgIds[0] = 24; // PDG ID for W boson (example)
    numSigEvents = bg_filtered->GetEntries();
    for (int i = 0; i < numSigEvents; ++i) {
        bg_filtered->GetEntry(i);
        // Example: Set momentum and energy based on the variables
        px[0] = ptsumf; py[0] = 0; pz[0] = 0; energy[0] = msumf;
        WriteEvent(lheFile, 1, pdgIds, statuses, px, py, pz, energy, mass);
    }

    lheFile << "</LesHouchesEvents>\n";
    lheFile.close();
    file->Close();
}

// Main function to run the test
void test2() {
    ConvertRootToLHE("../../mlpHiggs.root", "output.lhe");
}

int main() {
    test2();
    return 0;
}
