(* Quantum numbers for the hydrogen atom *)
n = 2; (* Principal quantum number *)
l = 1; (* Orbital angular momentum quantum number *)
m = 0; (* Magnetic quantum number *)

(* Bohr radius *)
a0 = 1; (* In atomic units, the Bohr radius is 1 *)

(* Radial part of the hydrogen wavefunction *)
Rnl[r_, n_, l_] := 
  Sqrt[(2/(n*a0))^3*Factorial[n - l - 1]/(2*n*Factorial[n + l])] * 
   Exp[-r/(n*a0)] * (2*r/(n*a0))^l * LaguerreL[n - l - 1, 2*l + 1, 2*r/(n*a0)];

(* Spherical Harmonic part *)
Ylm[theta_, phi_, l_, m_] := SphericalHarmonicY[l, m, theta, phi];

(* Full wavefunction *)
Psi[r_, theta_, phi_, n_, l_, m_] := 
  Rnl[r, n, l]*Ylm[theta, phi, l, m];

(* Plot the probability density |Psi|^2 in 3D space *)
plot = SphericalPlot3D[
   Abs[Psi[1, theta, phi, n, l, m]]^2, 
   {theta, 0, Pi}, {phi, 0, 2*Pi}, 
   PlotRange -> All, 
   PlotPoints -> 100, 
   Mesh -> None, 
   PlotStyle -> Directive[Orange, Opacity[0.7]],
   Boxed -> False, 
   Axes -> False, 
   PlotLabel -> 
    "Probability Density |Psi(r, θ, φ)|^2 for n=" <> 
     ToString[n] <> ", l=" <> ToString[l] <> ", m=" <> ToString[m]
   ];

(* Display the plot *)
plot

(* Save the plot as an image file *)
Export["HydrogenWavefunctionPlot.png", plot]
