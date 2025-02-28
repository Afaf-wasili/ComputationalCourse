#include <TFile.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TLegend.h>
#include <TStyle.h>
#include <TPad.h>
#include <iostream>
#include <cmath>  // For sqrt()

void SetupCustomStyle() {
    TStyle* customStyle = new TStyle("CustomStyle", "Custom Style for Plots");
    customStyle->SetCanvasColor(0);
    customStyle->SetPadColor(0);
    customStyle->SetFrameFillColor(0);
    customStyle->SetHistLineWidth(2);
    customStyle->SetLabelFont(132, "xyz");
    customStyle->SetLabelSize(0.04, "xyz");
    customStyle->SetTitleFont(130, "xyz");
    customStyle->SetTitleSize(0.03, "xyz");
    customStyle->SetTitleOffset(1.0, "xy");
    customStyle->SetLegendFont(132);
    customStyle->SetLegendTextSize(0.04);
    TGaxis::SetMaxDigits(3);
    TGaxis::SetExponentOffset(0.09, -0.09, "y");
    customStyle->SetPadGridX(true);
    customStyle->SetPadGridY(true);
    customStyle->SetGridWidth(1);
    customStyle->SetGridColor(kGray+2);
    customStyle->SetGridStyle(2);
    gROOT->SetStyle("CustomStyle");
    gStyle->cd();
    gStyle->SetPalette(84);
    gStyle->SetNumberContours(99);
    std::cout << "Custom style applied globally." << std::endl;
}

void overlapResidual() {
    SetupCustomStyle();
    gStyle->SetOptStat(0);  // Disable default statistics box

    std::string base_path = "/home/afafwasili/Datat_Muu/onebarlens";
    std::string file_nominal = base_path + "/shiftx_0/reco/residual_3_30.00_0.0000_6.00.root";
    std::string file_misaligned = base_path + "/shiftx_95/reco/residual_3_30.00_0.0000_6.00.root";

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

    TCanvas *c_nominal = (TCanvas*)f_nominal->Get("residual_3_30.00_0.0000_6.00");
    TCanvas *c_misaligned = (TCanvas*)f_misaligned->Get("residual_3_30.00_0.0000_6.00");

    if (!c_nominal || !c_misaligned) {
        std::cerr << "Error: TCanvas not found in one or both files!" << std::endl;
        f_nominal->Close();
        f_misaligned->Close();
        return;
    }

    TH1F *h_nominal = (TH1F*)c_nominal->GetListOfPrimitives()->FindObject("residual");
    TH1F *h_misaligned = (TH1F*)c_misaligned->GetListOfPrimitives()->FindObject("residual");

    if (!h_nominal || !h_misaligned) {
        std::cerr << "Error: Histogram not found inside the canvases!" << std::endl;
        f_nominal->Close();
        f_misaligned->Close();
        return;
    }

    // Compute statistics BEFORE normalization
    double mean_nominal = h_nominal->GetMean();
    double rms_nominal = h_nominal->GetRMS();
    double mean_nom_err = h_nominal->GetMeanError();
    double rms_nom_err = h_nominal->GetRMSError();

    double mean_misaligned = h_misaligned->GetMean();
    double rms_misaligned = h_misaligned->GetRMS();
    double mean_mis_err = h_misaligned->GetMeanError();
    double rms_mis_err = h_misaligned->GetRMSError();

    // Compute deltas (differences) and propagated errors
    double delta_mean = mean_misaligned - mean_nominal;
    double delta_rms = rms_misaligned - rms_nominal;
    double delta_mean_err = sqrt(mean_mis_err * mean_mis_err + mean_nom_err * mean_nom_err);
    double delta_rms_err = sqrt(rms_mis_err * rms_mis_err + rms_nom_err * rms_nom_err);

    // Normalize histograms
    h_nominal->Scale(1.0 / h_nominal->Integral(), "width");
    h_misaligned->Scale(1.0 / h_misaligned->Integral(), "width");

    TCanvas *c1 = new TCanvas("c1", "Residuals Comparison", 1200, 900);

    h_nominal->SetLineColor(kBlack);
    h_nominal->SetLineWidth(2);
    h_misaligned->SetLineColor(kGray + 1);
    h_misaligned->SetLineWidth(2);
    h_nominal->GetYaxis()->SetTitleOffset(1.8);

    h_nominal->GetXaxis()->SetTitleOffset(1.0);

    h_nominal->GetYaxis()->SetLabelSize(0.03);

    h_nominal->GetXaxis()->SetLabelSize(0.03);

    h_nominal->GetYaxis()->SetTitleFont(132);

    h_nominal->GetXaxis()->SetTitleFont(132);

    h_nominal->GetYaxis()->SetLabelFont(132);

    h_nominal->GetXaxis()->SetLabelFont(132);

    h_nominal->GetXaxis()->SetTitleSize(0.03);

    h_nominal->GetYaxis()->SetTitleSize(0.03);

    h_nominal->GetYaxis()->SetRangeUser(0,4.5);

    h_nominal->GetXaxis()->SetRangeUser(-1,2);
    h_nominal->GetYaxis()->SetTitleOffset(1.8);
    h_nominal->GetXaxis()->SetTitleOffset(1.0);
   
    h_nominal->GetXaxis()->SetRangeUser(-1,2);
    c1->SetGridx();
    c1->SetGridy();

    h_nominal->Draw("HIST");
    h_misaligned->Draw("HIST SAME");

    // Create a legend
    TLegend *legend = new TLegend(0.43, 0.7, 0.6, 0.90);
    legend->SetBorderSize(0);
    legend->SetFillStyle(0);
    legend->SetTextSize(0.025);
    legend->SetTextFont(132);
    legend->AddEntry((TObject*)0, "DIRC at ePIC: Misalignment only one bar with lens: rotation about Z", "");
    legend->AddEntry((TObject*)0, "Particle ID: #pi/K", "");
    legend->AddEntry((TObject*)0, "Track Angle: #theta = 30 [deg]", "");
    legend->AddEntry((TObject*)0, "Momentum: 6 GeV/c", "");

    // Add Nominal and Misaligned stats
    legend->AddEntry(h_nominal, Form("Nominal (#mu=%.4f #pm %.4f, RMS=%.4f #pm %.4f)", 
                                     mean_nominal, mean_nom_err, 
                                     rms_nominal, rms_nom_err), "l");
    legend->AddEntry(h_misaligned, Form("Misaligned (#mu=%.4f #pm %.4f, RMS=%.4f #pm %.4f)", 
                                        mean_misaligned, mean_mis_err, 
                                        rms_misaligned, rms_mis_err), "l");

    // Add Delta values
    legend->AddEntry((TObject*)0, Form("#Delta #mu = %.4f #pm %.4f", delta_mean, delta_mean_err), "");
    legend->AddEntry((TObject*)0, Form("#Delta RMS = %.4f #pm %.4f", delta_rms, delta_rms_err), "");

    legend->Draw();

    c1->SaveAs("Plots/histograms_with_delta.png");

    f_nominal->Close();
    f_misaligned->Close();
}


