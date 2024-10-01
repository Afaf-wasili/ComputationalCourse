import ROOT

# Define the path to the ROOT file
file_path = "../Matplotlib/Plots/histo.root"

# Open the ROOT file
file = ROOT.TFile(file_path, "READ")

# Retrieve the histograms
signal_hist = file.Get("data")  # Signal histogram

# Create a canvas
canvas = ROOT.TCanvas("canvas", "Data Histogram with Bayesian Confidence Intervals", 800, 600)

# Draw the signal histogram
signal_hist.SetLineColor(ROOT.kBlue)
signal_hist.SetTitle("Data Histogram with Bayesian Confidence Intervals")
signal_hist.GetXaxis().SetTitle("X axis")
signal_hist.GetYaxis().SetTitle("Counts")
signal_hist.Draw("HIST")

# Define prior parameters for Bayesian intervals (adjusted)
prior_alpha = 1  # Prior counts for signal
prior_beta = 1   # Prior counts for background
confidence_level = 0.95
alpha = 1 - confidence_level

# Function to compute Bayesian intervals
def compute_bayesian_intervals(counts, prior_alpha, alpha):
    lower_bounds = []
    upper_bounds = []
    
    for count in counts:
        # Using an approximation for the Bayesian intervals
        total_count = count + prior_alpha
        
        # Lower bound using the normal approximation for small counts
        lower_bound = ROOT.TMath.ChisquareQuantile(alpha / 2, 2 * (total_count)) / 2
        upper_bound = ROOT.TMath.ChisquareQuantile(1 - alpha / 2, 2 * (total_count + 1)) / 2

        lower_bounds.append(max(lower_bound, 0))  # Ensure non-negative
        upper_bounds.append(upper_bound)

    return lower_bounds, upper_bounds

# Compute Bayesian intervals for the data histogram
data_values = [signal_hist.GetBinContent(i) for i in range(1, signal_hist.GetNbinsX() + 1)]
data_lower_bounds, data_upper_bounds = compute_bayesian_intervals(data_values, prior_alpha, alpha)

# Create histograms for Bayesian confidence intervals
n_bins = signal_hist.GetNbinsX()
bayesian_hist_lower = ROOT.TH1F("bayesian_hist_lower", "", n_bins, 0, n_bins)
bayesian_hist_upper = ROOT.TH1F("bayesian_hist_upper", "", n_bins, 0, n_bins)

# Fill the confidence interval histograms
for i in range(1, n_bins + 1):
    bayesian_hist_lower.SetBinContent(i, data_lower_bounds[i - 1])
    bayesian_hist_upper.SetBinContent(i, data_upper_bounds[i - 1])

# Set colors for the confidence interval histograms
bayesian_hist_lower.SetFillColor(ROOT.kGreen)
bayesian_hist_upper.SetFillColor(ROOT.kRed)

# Draw the confidence interval histograms
bayesian_hist_lower.Draw("SAME HIST")
bayesian_hist_upper.Draw("SAME HIST")

# Create legend
legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(signal_hist, "Data", "l")
legend.AddEntry(bayesian_hist_lower, "95% Bayesian Lower CI", "f")
legend.AddEntry(bayesian_hist_upper, "95% Bayesian Upper CI", "f")
legend.Draw()

# Save the plot
canvas.SaveAs("Plots/data_histogram_with_bayesian_intervals.png")

# Close the ROOT file
file.Close()
