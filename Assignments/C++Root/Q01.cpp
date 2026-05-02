#include "style.h"

void gaussianfit_acolin(){

  SetGlobalStyle();

  // =========================
  // OPEN FILE
  // =========================
  TFile *file = TFile::Open("mlpHiggs.root");

  // =========================
  // QUESTION (0):
  // Get the SIGNAL tree "sig_filtered"
  // =========================



  // =========================
  // VARIABLE
  // =========================
  float sig_acolin = 0;

  // =========================
  // QUESTION (1):
  // Set branch address for "acolin"
  // =========================



  // =========================
  // HISTOGRAM
  // =========================
  TH1F *h = new TH1F("h","Signal acolin",50,0,3);

  // =========================
  // QUESTION (2):
  // Fill histogram using loop over sig_tree
  // =========================



  // =========================
  // CANVAS
  // =========================
  TCanvas *c = new TCanvas("c","Gaussian Fit (acolin)",800,600);
  SetCanvasStyle(c);

  // =========================
  // STYLE HISTOGRAM
  // =========================
  SetHistogramStyle(h);

  // =========================
  // QUESTION (3):
  // Set axis labels:
  //   X-axis → "Acolinearity"
  //   Y-axis → "Events"
  // =========================



  // =========================
  // DRAW HISTOGRAM
  // =========================
  h->Draw("HIST");

  // =========================
  // QUESTION (4):
  // Create Gaussian function and fit histogram
  // Hint: choose a reasonable fit range
  // =========================



  // =========================
  // QUESTION (5):
  // Extract:
  //   mean
  //   sigma
  //   mean error
  //   sigma error
  // =========================



  // =========================
  // QUESTION (6):
  // Create legend and display results

  //
  // Hint:  leg->AddEntry((TObject*)0,
  //      Form("#mu = %.3f #pm %.3f", mean, mean_err), "");
  //

  // =========================



  // =========================
  // QUESTION (7):
  // Save the canvas as:
  //   "acolin_gaussian_fit.png"
  // =========================

}
