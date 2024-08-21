(* Parameters *)
rho1 = 0.8;
rho2 = 1;
km3 = 31.4358;

(* Simplified Monte Carlo Integration *)
nSamples = 1000; (* Reasonable sample size *)
randomPoints = RandomReal[{rho1, rho2}, nSamples];
integrand = Function[x, x * (BesselJ[1/2, km3 * x] +
    (-D[BesselJ[1/2, x], x]) / (D[BesselY[1/2, x], x]) -
     2 * Pi * Cos[x] / x - 2 * Pi * Sin[x] / x * BesselY[1/2, km3 * x])^2];

(* Calculate Monte Carlo Integral *)
mcValues = integrand /@ randomPoints;
mcIntegral = Mean[mcValues] * (rho2 - rho1);

(* Debug output *)
Print["Monte Carlo integral values: ", mcValues[[1 ;; 10]]]; (* Print first 10 values for inspection *)
Print["Monte Carlo integration result: ", mcIntegral];

(* Calculate normalization factor *)
bm1 = Pi * mcIntegral;
am1 = 1 / Sqrt[bm1];

(* Output the normalization factor *)
Print["Normalization factor (am1): ", am1];

(* Simplified Function for Plotting *)
F1Simplified[theta_, phi_] :=
  Abs[am1 * Cos[theta] * Exp[-I * km3 * rho1 * Cos[phi] * Sin[theta]]] / 2;

(* Debugging - Check value range of F1Simplified *)
debugValues = Table[F1Simplified[theta, phi], {theta, 0, Pi, Pi/10}, {phi, 0, 2*Pi, Pi/10}];
Print["Sample values of F1Simplified: ", debugValues];

(* Generate a Simplified Plot *)
plot = SphericalPlot3D[
   F1Simplified[theta, phi],
   {theta, 0, Pi},
   {phi, 0, 2*Pi},
   PlotPoints -> 100,  (* Increased for better resolution *)
   PlotRange -> All,
   Axes -> False,
   Boxed -> False
];

(* Export Plot *)
Export["mc_optimized_plot.png", plot];
Print["Plot saved as 'mc_optimized_plot.png'"];
