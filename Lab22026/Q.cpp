#include "style.h"

void sigeffpurity() {

    SetGlobalStyle();

    // =========================
    // OPEN FILE
    // =========================

    TFile *file = TFile::Open("mlpHiggs.root");


    // =========================
    // GET TREES
    // =========================

    TTree *sig=(TTree*)file->Get("sig_filtered");

    // Q1(a) [1 Mark]
    //
    // Define background tree and
    // complete the command

    TTree *bg = ___________________;



    // =========================
    // TOTAL EVENTS
    // =========================

    int Ns=sig->GetEntries();

    int Nb=bg->GetEntries();



    // Q1(b) [1 Mark]
    //
    // Define variables and apply
    // SetBranchAddress()

    _______________________;

    _______________________;

    _______________________;

    _______________________;



    // =========================
    // GRAPHS
    // =========================

    TGraphErrors *g_eff=
    new TGraphErrors();


    // Q2 [2 Marks]
    //
    // Create purity and product
    // graphs using TGraphErrors

    TGraphErrors *g_pur=
    ____________________;

    TGraphErrors *g_prod=
    ____________________;



    for(int t=80;t<=200;t++){

        int count_sig=0;
        int count_bg=0;


        // Signal loop already completed

        for(int i=0;i<Ns;i++){

            sig->GetEntry(i);

            if(sig_acolin>=t)

                count_sig++;
        }



        // Q3 [1 Mark]
        //
        // Complete only the
        // background selection
        //
        // Condition:
        //
        // bg_acolin >= threshold

        for(int i=_____________){

            __________________;

            if(________________)

                count_bg++;

        }



        // Q4(a) [1 Mark]
        //
        // Calculate:
        //
        // Efficiency
        // Binomial error

        double eff=
        ____________________;

        double err=
        ____________________;


        int p=g_eff->GetN();

        g_eff->SetPoint(p,t,eff);

        g_eff->SetPointError(p,0,err);



        double purity=0;

        if((count_sig+count_bg)>0)

        purity=
        (double)count_sig/
        (count_sig+count_bg);


        int p2=g_pur->GetN();

        g_pur->SetPoint(p2,t,purity);



        // Q4(b) [1 Mark]
        //
        // Calculate:
        //
        // Product =
        // Efficiency * Purity

        double product=
        ___________________;


        int p3=g_prod->GetN();

        g_prod->SetPoint(p3,t,product);

    }



    g_eff->SetLineColor(kBlue);

    g_pur->SetLineColor(kRed);

    g_prod->SetLineColor(kGreen+2);



    TCanvas *c=
    new TCanvas("c","",800,600);

    SetCanvasStyle(c);



    // Q5(a) [1 Mark]
    //
    // Draw purity and product
    // on the same canvas

    g_eff->Draw("ALP");

    _____________________;

    _____________________;



    // Q5(b) [1 Mark]
    //
    // Add legend entries and explain:
    //
    // Efficiency
    // Purity
    // Efficiency * Purity

    TLegend *leg=
    new TLegend(
    0.65,0.70,0.88,0.88);

    _____________________;

    _____________________;

    _____________________;

    leg->Draw();



    // Q5(c) [1 Mark]
    //
    // Save result as png

    _____________________;

}
