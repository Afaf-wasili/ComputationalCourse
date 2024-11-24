/*
You are given a ROOT file with two trees: sig_filtered (signal events) and bg_filtered (background events). 
The goal is to calculate the efficiency for signal events as a function of the acollinearity threshold (acolin) 
and plot it alongside its 95% Confidence Intervals (CL).

Instructions:
1. Use the following equations for confidence intervals:
   Lower Bound = p - z * sqrt(p * (1 - p) / n)
   Upper Bound = p + z * sqrt(p * (1 - p) / n)
   where:
     - p = efficiency (signal count / total signal events)
     - z = 1.96 (for 95% CL)
     - n = total signal events.

2. Write a ROOT macro or C++ program to:
   - Loop over acollinearity thresholds from 80 to 200.
   - Calculate efficiency and confidence intervals for each threshold.
   - Plot:
       * Efficiency as a blue line with markers.
       * Confidence intervals as dashed lines in a different color.

3. Label the plot:
   - X-axis: Acollinearity threshold (degrees).
   - Y-axis: Efficiency.
   - Include a legend for efficiency and confidence intervals.
*/
