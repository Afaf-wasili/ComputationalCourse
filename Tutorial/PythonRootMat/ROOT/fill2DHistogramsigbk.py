import ROOT

def fill2DHistogram():
    ROOT.gStyle.SetPalette(ROOT.kRainBow)

    # Open the ROOT file and retrieve histograms
    file = ROOT.TFile.Open("mlpHiggs.root")

    # Retrieve signal and background trees
    sig_tree = file.Get("sig_filtered")
    bg_tree = file.Get("bg_filtered")

    # Create a 2D histogram using binning for background vs signal
    nbins_x = 100  # Set number of bins for x-axis (Background)
    nbins_y = 100  # Set number of bins for y-axis (Signal)
    x_min = 0      # Set minimum value for x-axis (change as needed)
    x_max = 180    # Set maximum value for x-axis (change as needed)
    y_min = 0      # Set minimum value for y-axis (change as needed)
    y_max = 180    # Set maximum value for y-axis (change as needed)

    # Create a 2D histogram
    hist_2d = ROOT.TH2F("hist_2d", "Background vs Signal;Background;Signal",
                         nbins_x, x_min, x_max,
                         nbins_y, y_min, y_max)

    # Loop over background entries and fill the 2D histogram
    for j in range(bg_tree.GetEntries()):
        bg_tree.GetEntry(j)
        # Fill with the background variable on the x-axis and some variable from signal tree
        # Adjust this line according to your specific analysis
        for i in range(sig_tree.GetEntries()):
            sig_tree.GetEntry(i)
            # Fill the histogram using the chosen variables from both trees
            hist_2d.Fill(bg_tree.acolin, sig_tree.acolin)  # Replace acolin with actual variable names

    # Draw the 2D histogram
    c = ROOT.TCanvas("c", "Background vs Signal", 800, 600)
    hist_2d.Draw("COLZ")

    # Add a color bar
    color_bar = ROOT.TPaletteAxis(1, 0, 1, 1, hist_2d.GetMinimum(), hist_2d.GetMaximum())
    color_bar.SetTitle("Counts")
    color_bar.Draw()

    # Show the canvas
    c.Show()

    # Optionally save the canvas
    # c.SaveAs("Plots/Background_Signal_2D_Histogram.png")

    # Close the ROOT file
    file.Close()
    ROOT.gApplication.Run()

# Run the function
fill2DHistogram()
