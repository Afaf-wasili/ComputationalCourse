import ROOT as R
from random import gauss

# Create a one dimensional histogram
hist = R.TH1F("gauss", "Gaussian distribution", 10, -3, 3)

# Fill the histogram with random numbers
for i in range(100):
    hist.Fill(gauss(0, 1))

# Create a ROOT file
f = R.TFile("gauss.root", "RECREATE")
# Write the histogram to the file and close it
hist.Write()
f.Close()
