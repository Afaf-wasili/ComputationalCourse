
void readtxt(){
// Apply the modern style
    gROOT->SetStyle("ATLAS");
    gROOT->ForceStyle();

    // Set font for axis titles and labels
    gStyle->SetLabelFont(22, "X");
    gStyle->SetLabelFont(22, "Y");
    gStyle->SetTitleFont(22, "X");
    gStyle->SetTitleFont(22, "Y");

    // Set size of axis titles and labels
    gStyle->SetLabelSize(0.03, "X");
    gStyle->SetLabelSize(0.03, "Y");
    gStyle->SetTitleSize(0.04, "X");
    gStyle->SetTitleSize(0.04, "Y");
    gStyle->SetMarkerSize(0.5);



  //open file
  std::ifstream infile("data.txt");

  //vectors to store data
  std::vector<double> mass, angle;

  //READ
  
  for (double a, m; infile >> m >> a;){
    mass.push_back(m);
    angle.push_back(a);
    }
  /*
  double m, a;
  
  while(infile >> m >> a){
    mass.push_back(m);                                                                       
    angle.push_back(a);

    }*/

  //plotting
  TGraph* graph = new TGraph(angle.size(), mass.data(), angle.data());
  graph->SetTitle("mass vs angle; mass; angle ");
  graph->SetMarkerStyle(20);
  graph->SetLineStyle(2);
  graph->SetLineColor(8);
  graph->SetMarkerColor(8);
  TCanvas* canvas = new TCanvas();
  graph->Draw("APL");
  canvas->SaveAs("Plots/readtxt.png");
  


}









