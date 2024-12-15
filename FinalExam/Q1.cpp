
//Question-1 K&U (CLO1.1)-10points:
/*
Question-1a: 
Reading Data from a Text File which is avaliable in your directory and Plotting with ROOT:
    1- Initialize containers or vaiables as considering the first column (mass) and the second (angle) to store the data
    2- Implement the loop to read data from the file and store in containers
    3- Create a TGraph from the data
    4- Customize the graph's appearance
    5- Draw the graph with labling on a canvas
    6- Save the plot as a PNG file

*/

#include <iostream>
#include <fstream>
#include <vector>
#include <TGraph.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TROOT.h>

void readtxt() {
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

    // Open the file "data.txt" for reading
    std::ifstream infile("data.txt");
    if (!infile.is_open()) {
        std::cerr << "Error opening file 'data.txt'" << std::endl;
        return;
    }

    // Containers to store the data
    std::vector<double> mass;
    std::vector<double> angle;

}


/*
Question-1b:
1- Define Variables in the Header File
2- Use main function instead of void function and calling 
*/


void Q1(){ 

  std::cout << "Addition: " << (a + b) << std::endl;
    std::cout << "Subtraction: " << (a - b) << std::endl;
    std::cout << "Multiplication: " << (a * b) << std::endl;
    std::cout << "Division: " << (a / b) << std::endl;

    std::cout << "Modulo: " << (x % y) << std::endl;

    std::cout << "Power: " << pow(a, b) << std::endl;
    std::cout << "Square Root: " << sqrt(a) << std::endl;

}
