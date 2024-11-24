void test() {
    // Apply the modern style
    gROOT->SetStyle("ATLAS");
    gROOT->ForceStyle();

    gStyle->SetLabelFont(22, "X");
    gStyle->SetLabelFont(22, "Y");
    gStyle->SetTitleFont(22, "X");
    gStyle->SetTitleFont(22, "Y");
    gStyle->SetLabelSize(0.03, "X");
    gStyle->SetLabelSize(0.03, "Y");
    gStyle->SetTitleSize(0.04, "X");
    gStyle->SetTitleSize(0.04, "Y");
    gStyle->SetLegendFont(22);

    // Define the absolute path to the ROOT file
    const char* file_path = "histo.root";

    // Open the ROOT file
    TFile* file = TFile::Open(file_path, "READ");
    if (!file || file->IsZombie()) {
        printf("Error opening file: %s\n", file_path);
        return;
    }

    // Retrieve the data histogram
    TH1* data_hist = (TH1*)file->Get("data");
    if (!data_hist || data_hist->GetEntries() == 0) {
        printf("Histogram 'data' is missing or empty.\n");
        file->Close();
        return;
    }

    // Debugging: Print the number of entries
    printf("Histogram 'data' has %f entries.\n", data_hist->GetEntries());

    // Set up the canvas
    TCanvas* canvas = new TCanvas("canvas", "Data Histogram with Gaussian Fit", 800, 600);
    canvas->SetMargin(0.15, 0.05, 0.15, 0.1);

    // Set colors and remove statistics box
    data_hist->SetLineColor(kBlue);
    data_hist->SetStats(0);

    // Draw the histogram
    data_hist->Draw("HIST");
    data_hist->GetXaxis()->SetTitle("Mass");
    data_hist->GetYaxis()->SetTitle("Counts");

    // Create and fit the Gaussian function
    TF1* gauss = new TF1("gauss", "gaus", 70, 120);
    gauss->SetParLimits(0, 220, 300);

    data_hist->Fit(gauss, "");
    gauss->SetLineColor(kRed);
    //gauss->Draw("SAME");

    // Legend setup
    TLegend* legend = new TLegend(0.7, 0.7, 0.9, 0.9);
    double mean = gauss->GetParameter(1);
    double sigma = gauss->GetParameter(2);
    double mean_error = gauss->GetParError(1);
    double sigma_error = gauss->GetParError(2);

    legend->AddEntry(data_hist, "Data", "l");
    legend->AddEntry(gauss, "Gaussian Fit", "l");
    legend->AddEntry((TObject*)0, Form("#mu: %.2f #pm %.3f", mean, mean_error), "");
    legend->AddEntry((TObject*)0, Form("#sigma: %.2f #pm %.3f", sigma, sigma_error), "");
    legend->Draw();

    // Save the canvas
    system("mkdir -p Plots"); // Ensure directory exists
    canvas->SaveAs("Plots/Data_Histogram_with_Gaussian_Fit_and_Errors.png");

    // Close the ROOT file
    file->Close();
}
