#ifndef STYLE_H
#define STYLE_H

#include <TCanvas.h>
#include <TH1.h>
#include <TF1.h>
#include <TLegend.h>
#include <TStyle.h>

void SetGlobalStyle() {
  gStyle->SetOptStat(0);
    gStyle->SetOptFit(0);
}

void SetHistogramStyle(TH1 *h) {
    h->SetLineColor(kBlue);
    h->SetLineWidth(2);
    h->SetStats(0);

    // AXIS TITLE SETTINGS
    h->GetXaxis()->SetTitleSize(0.04);
    h->GetXaxis()->SetTitleOffset(1.3);
    h->GetXaxis()->SetLabelSize(0.03);

    h->GetYaxis()->SetTitleSize(0.04);
    h->GetYaxis()->SetTitleOffset(1.3);
    h->GetYaxis()->SetLabelSize(0.03);
}

void SetFitStyle(TF1 *f) {
    f->SetLineColor(kRed);
    f->SetLineWidth(2);
    f->SetLineStyle(1);
}

void SetCanvasStyle(TCanvas *c) {
    c->SetGrid();               // Enable grid
    c->SetGridx(1);             // Grid on X axis
    c->SetGridy(1);             // Grid on Y axis
    c->SetFrameBorderMode(0);

    // Margins for titles
    c->SetLeftMargin(0.15);
    c->SetBottomMargin(0.15);
    c->SetRightMargin(0.05);
    c->SetTopMargin(0.08);
}


TLegend* CreateLegend() {
    TLegend *leg = new TLegend(0.65, 0.75, 0.88, 0.88);
    leg->SetBorderSize(0);
    leg->SetFillStyle(0);
    leg->SetTextSize(0.03);
    return leg;
}

#endif
