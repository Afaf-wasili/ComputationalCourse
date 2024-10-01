import ROOT

def plot_efficiency():
    # Open the ROOT file
    file_path = "random_signal_background.root"  # Change to your file path
    file = ROOT.TFile(file_path, "READ")

    # Retrieve the histogram for signal
    signal_hist = file.Get("histProton")  # Change to your actual histogram name

    # Check if the histogram was retrieved correctly
    if not signal_hist:
        print("Error: Signal histogram not found!")
        return

    # Calculate the total number of signal events
    total_signal_events = signal_hist.Integral()  # Total events in the signal histogram

    # Set mass range for detected events (example: between 0.8 and 1.2 GeV/c^2)
    mass_range_min = 0.8
    mass_range_max = 1.2

    # Calculate detected signal events in the specified mass range
    detected_signal_events = signal_hist.Integral(signal_hist.FindBin(mass_range_min),
                                                   signal_hist.FindBin(mass_range_max))

    # Calculate efficiency
    efficiency = (detected_signal_events / total_signal_events) if total_signal_events > 0 else 0

    # Create a histogram to plot efficiency
    efficiency_hist = ROOT.TH1F("efficiency_hist", "Efficiency", 1, 0, 1)
    efficiency_hist.SetBinContent(1, efficiency)  # Set efficiency value in the first bin
    efficiency_hist.SetBinError(1, 0)  # Set error to zero or calculate if needed

    # Set titles
    efficiency_hist.GetXaxis().SetTitle("Efficiency")
    efficiency_hist.GetYaxis().SetTitle("Value")

    # Create a canvas for drawing
    canvas = ROOT.TCanvas("canvas", "Efficiency", 800, 600)

    # Draw the efficiency histogram
    efficiency_hist.Draw("E")

    # Save the canvas as an image
    canvas.SaveAs("efficiency_plot.png")

    # Close the ROOT file
    file.Close()

# Call the function to plot efficiency
plot_efficiency()
