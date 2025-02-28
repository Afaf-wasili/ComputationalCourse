#include <TFile.h>

#include <TCanvas.h>

#include <TH1F.h>

#include <TLegend.h>

#include <TStyle.h>

#include <TPad.h>

#include <iostream>



void SetupCustomStyle() {

    TStyle* customStyle = new TStyle("CustomStyle", "Custom Style for Plots");

    customStyle->SetCanvasColor(0);

    customStyle->SetPadColor(0);

    customStyle->SetFrameFillColor(0);

    customStyle->SetHistLineWidth(2);

    customStyle->SetLabelFont(132, "x");

    customStyle->SetLabelFont(132, "y");

    customStyle->SetLabelFont(132, "z");

    customStyle->SetLabelSize(0.04, "x");

    customStyle->SetLabelSize(0.04, "y");

    customStyle->SetLabelSize(0.04, "z");

    customStyle->SetTitleFont(130, "x");

    customStyle->SetTitleFont(130, "y");

    customStyle->SetTitleFont(130, "z");

    customStyle->SetTitleSize(0.03, "x");

    customStyle->SetTitleSize(0.03, "y");

    customStyle->SetTitleSize(0.03, "z");

    customStyle->SetLegendFont(132);

    customStyle->SetLegendTextSize(0.03);

    TGaxis::SetMaxDigits(3);

    TGaxis::SetExponentOffset(0.09, -0.09, "y");

    customStyle->SetPadGridX(true);

    customStyle->SetPadGridY(true);

    customStyle->SetGridWidth(1);

    customStyle->SetGridColor(kGray+2);

    customStyle->SetGridStyle(2);

    gROOT->SetStyle("CustomStyle");

    gStyle->cd();

    std::cout << "Custom style applied globally." << std::endl;

}



void overlapmeasuredangle() {

    SetupCustomStyle();

    gStyle->SetOptStat(0);  



    // Define ROOT file paths

    std::string base_path = "/home/afafwasili/Datat_Muu/onebarlens";

    std::string file_nominal = base_path + "/shiftx_0/reco/tangle_3_30.00_0.0000_6.00.root";

    std::string file_misaligned = base_path + "/shiftx_80/reco/tangle_3_30.00_0.0000_6.00.root";



    // Open ROOT files

    TFile *f_nominal = TFile::Open(file_nominal.c_str(), "READ");

    TFile *f_misaligned = TFile::Open(file_misaligned.c_str(), "READ");



    if (!f_nominal || f_nominal->IsZombie()) {

        std::cerr << "Error: Cannot open " << file_nominal << std::endl;

        return;

    }

    if (!f_misaligned || f_misaligned->IsZombie()) {

        std::cerr << "Error: Cannot open " << file_misaligned << std::endl;

        return;

    }



    // Retrieve histograms from ROOT files

    TCanvas *c_nominal = (TCanvas*)f_nominal->Get("tangle_3_30.00_0.0000_6.00");

    TCanvas *c_misaligned = (TCanvas*)f_misaligned->Get("tangle_3_30.00_0.0000_6.00");



    if (!c_nominal || !c_misaligned) {

        std::cerr << "Error: TCanvas not found in one or both files!" << std::endl;

        f_nominal->Close();

        f_misaligned->Close();

        return;

    }



    // Extract both peaks from the histograms

    TH1F *h_nominal_K = (TH1F*)c_nominal->GetListOfPrimitives()->FindObject("thetac_3");

    TH1F *h_nominal_pi = (TH1F*)c_nominal->GetListOfPrimitives()->FindObject("thetac_2");



    TH1F *h_misaligned_K = (TH1F*)c_misaligned->GetListOfPrimitives()->FindObject("thetac_3");

    TH1F *h_misaligned_pi = (TH1F*)c_misaligned->GetListOfPrimitives()->FindObject("thetac_2");



    if (!h_nominal_K || !h_nominal_pi || !h_misaligned_K || !h_misaligned_pi) {

        std::cerr << "Error: One or more histograms not found!" << std::endl;

        f_nominal->Close();

        f_misaligned->Close();

        return;

    }



    // Normalize histograms

    h_nominal_K->Scale(1.0 / h_nominal_K->Integral(), "width");

    h_nominal_pi->Scale(1.0 / h_nominal_pi->Integral(), "width");

    h_misaligned_K->Scale(1.0 / h_misaligned_K->Integral(), "width");

    h_misaligned_pi->Scale(1.0 / h_misaligned_pi->Integral(), "width");



    // Compute statistics AFTER normalization

double mean_nominal_K_err = h_nominal_K->GetMeanError();
double rms_nominal_K_err = h_nominal_K->GetRMSError();
double mean_nominal_pi_err = h_nominal_pi->GetMeanError();
double rms_nominal_pi_err = h_nominal_pi->GetRMSError();

double mean_misaligned_K_err = h_misaligned_K->GetMeanError();
double rms_misaligned_K_err = h_misaligned_K->GetRMSError();
double mean_misaligned_pi_err = h_misaligned_pi->GetMeanError();
double rms_misaligned_pi_err = h_misaligned_pi->GetRMSError();

// Compute errors for differences
double delta_mean_K_err = sqrt(mean_misaligned_K_err * mean_misaligned_K_err +
                               mean_nominal_K_err * mean_nominal_K_err);
double delta_rms_K_err = sqrt(rms_misaligned_K_err * rms_misaligned_K_err +
                              rms_nominal_K_err * rms_nominal_K_err);
double delta_mean_pi_err = sqrt(mean_misaligned_pi_err * mean_misaligned_pi_err +
                                mean_nominal_pi_err * mean_nominal_pi_err);
double delta_rms_pi_err = sqrt(rms_misaligned_pi_err * rms_misaligned_pi_err +
                               rms_nominal_pi_err * rms_nominal_pi_err);

    
    double mean_nominal_K = h_nominal_K->GetMean();

    double rms_nominal_K = h_nominal_K->GetRMS();

    double mean_nominal_pi = h_nominal_pi->GetMean();

    double rms_nominal_pi = h_nominal_pi->GetRMS();



    double mean_misaligned_K = h_misaligned_K->GetMean();

    double rms_misaligned_K = h_misaligned_K->GetRMS();

    double mean_misaligned_pi = h_misaligned_pi->GetMean();

    double rms_misaligned_pi = h_misaligned_pi->GetRMS();



    // Compute differences

    double delta_mean_K = mean_misaligned_K - mean_nominal_K;

    double delta_rms_K = rms_misaligned_K - rms_nominal_K;

    double delta_mean_pi = mean_misaligned_pi - mean_nominal_pi;

    double delta_rms_pi = rms_misaligned_pi - rms_nominal_pi;



    // Set colors

    h_nominal_K->SetLineColor(kGreen+1);

    h_nominal_pi->SetLineColor(kGreen+3);

    h_nominal_K->SetLineWidth(2);

    h_nominal_pi->SetLineWidth(2);

    h_nominal_K->SetLineStyle(2);  // Dashed line for Nominal K

    h_nominal_pi->SetLineStyle(2);  // Dashed line for Nominal π



 

    h_misaligned_K->SetLineColor(kGray+1);

    h_misaligned_pi->SetLineColor(kGray+3);

    h_misaligned_K->SetLineWidth(2);

    h_misaligned_pi->SetLineWidth(2);



    // Create a canvas

    TCanvas *c1 = new TCanvas("c1", "Residuals Comparison", 1300, 900);

    c1->SetGridx();

    c1->SetGridy();

    h_nominal_K->GetYaxis()->SetTitleOffset(1.5);

    h_nominal_K->GetXaxis()->SetTitleOffset(1.5);

    h_nominal_K->GetYaxis()->SetLabelSize(0.03);

    h_nominal_K->GetXaxis()->SetLabelSize(0.03);

    h_nominal_K->GetYaxis()->SetTitleFont(132);

    h_nominal_K->GetXaxis()->SetTitleFont(132);

    h_nominal_K->GetYaxis()->SetLabelFont(132);

    h_nominal_K->GetXaxis()->SetLabelFont(132);

    h_nominal_K->GetXaxis()->SetTitleSize(0.03);

    h_nominal_K->GetYaxis()->SetTitleSize(0.03);
    h_nominal_K->GetXaxis()->SetRangeUser(0,0.1);

    // Style axes

    h_nominal_K->GetYaxis()->SetTitle("Entries [#]");

    h_nominal_K->GetXaxis()->SetTitle("#theta_{C} [rad]");

    //        h_nominal_K->GetXaxis()->SetRangeUser(0.7, 1.2);

    // Plot histograms

    h_nominal_K->Draw("HIST");

    h_nominal_pi->Draw("HIST SAME");

    h_misaligned_K->Draw("HIST SAME");

    h_misaligned_pi->Draw("HIST SAME");



    // Create a legend

    //        TLegend *legend = new TLegend(0.43, 0.7, 0.85, 0.90);

    TLegend *legend = new TLegend(0.55, 0.6, 0.9, 0.90);



    legend->SetBorderSize(0);

    legend->SetFillStyle(0);

    legend->SetTextSize(0.023);

    legend->SetTextFont(132);

     legend->AddEntry((TObject*)0, "DIRC at ePIC: Misalignment only one bar with lens", "");



     legend->AddEntry((TObject*)0, "Offset in X (Work in Progress)", "");

    legend->AddEntry((TObject*)0, "Particle ID: #pi/K", "");

    legend->AddEntry((TObject*)0, "Track Angle: #theta = 30 [deg]", "");

    legend->AddEntry((TObject*)0, "Momentum: 6 GeV/c", "");


    legend->AddEntry(h_nominal_K, Form("Nominal K (#mu=%.4f #pm %.4f, RMS=%.4f #pm %.4f)",
                                   mean_nominal_K, mean_nominal_K_err,
                                   rms_nominal_K, rms_nominal_K_err), "l");
legend->AddEntry(h_nominal_pi, Form("Nominal #pi (#mu=%.4f #pm %.4f, RMS=%.4f #pm %.4f)",
                                    mean_nominal_pi, mean_nominal_pi_err,
                                    rms_nominal_pi, rms_nominal_pi_err), "l");
legend->AddEntry(h_misaligned_K, Form("Misaligned K (#mu=%.4f #pm %.4f, RMS=%.4f #pm %.4f)",
                                      mean_misaligned_K, mean_misaligned_K_err,
                                      rms_misaligned_K, rms_misaligned_K_err), "l");
legend->AddEntry(h_misaligned_pi, Form("Misaligned #pi (#mu=%.4f #pm %.4f, RMS=%.4f #pm %.4f)",
                                       mean_misaligned_pi, mean_misaligned_pi_err,
                                       rms_misaligned_pi, rms_misaligned_pi_err), "l");

// Update Δμ and Δσ with propagated errors
legend->AddEntry((TObject*)0, Form("K: #Delta #mu = %.4f #pm %.4f, #Delta RMS = %.4f #pm %.4f",
                                   delta_mean_K, delta_mean_K_err,
                                   delta_rms_K, delta_rms_K_err), "");
legend->AddEntry((TObject*)0, Form("#pi: #Delta #mu = %.4f #pm %.4f, #Delta RMS = %.4f #pm %.4f",
                                   delta_mean_pi, delta_mean_pi_err,
                                   delta_rms_pi, delta_rms_pi_err), "");
legend->Draw();




    c1->SaveAs("Plots/multiple_peaks_comparison.png");

}


