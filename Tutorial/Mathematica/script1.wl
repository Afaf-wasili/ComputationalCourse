(* Define constants *)
rho1 = 0.8;
rho2 = 1;
km3 = 31.4358;
a = rho1 / rho2;
x13 = 31.4358;

(* Calculate cm1 *)
cm1 = (-D[BesselJ[1/2, x], x]) / (D[BesselY[1/2, x], x]) - 2 * π * Cos[x] / x - 2 * π * Sin[x] / x;

(* Numerical integration for bm1 *)
bm1 = π * NIntegrate[x * (BesselJ[1/2, km3 * x] + cm1 * BesselY[1/2, km3 * x])^2, {x, rho1, rho2}];

(* Compute am1 *)
am1 = 1 / Sqrt[bm1];

(* Define psi1n and F1, F2 *)
psi1n1 = am1 * (BesselJ[1/2, km3 * rho1] + cm1 * BesselY[1/2, km3 * rho1]) * Cos[1/2 * phip];
F1 = rho1 * psi1n1 * Exp[-I * km3 * rho1 * (Cos[phi - phip] * Sin[theta])];

psi1n2 = am1 * (BesselJ[1/2, km3 * rho2] + cm1 * BesselY[1/2, km3 * rho2]) * Cos[1/2 * phip];
F2 = rho2 * psi1n2 * Exp[-I * km3 * rho2 * (Cos[phi - phip] * Sin[theta])];

(* Define Ruqayyah with proper substitution *)
psi1np = psi1n1 /. phip -> Pi - 0.0000001;
Ruqayyah = rho * psi1np * Exp[-I * km3 * rho * (Cos[phi - Pi + 0.0000001] * Sin[theta])];

(* Plot using SphericalPlot3D*)
SphericalPlot3D[
  Sin[theta]^2 * Abs[NIntegrate[F1, {phip, 0, 2 * Pi}] - NIntegrate[F2, {phip, 0, 2 * Pi}] + 2 * NIntegrate[Ruqayyah, {rho, rho1, rho2}]]^2,
  {theta, 0, Pi},
  {phi, 0, 2 * Pi},
  PlotPoints -> 50,  (* Increase PlotPoints for better resolution *)
  PlotRange -> All,
  Axes -> False,
  Boxed -> False
];


(* Save the plot as an image file *)
Export["plot.png", plot];