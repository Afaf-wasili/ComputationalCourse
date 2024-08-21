#include <TCanvas.h>
#include <TH3F.h>
#include <TF1.h>
#include <TMath.h>
#include <complex>
#include <boost/math/special_functions/bessel.hpp>
#include <boost/math/integration/quadrature.hpp>

using namespace std;
using namespace boost::math;
using namespace boost::math::quadrature;

void plot() {
    double rho1 = 0.8;
    double rho2 = 1;
    double km3 = 31.4358;
    double a = rho1 / rho2;
    double x13 = 31.4358;

    // Define Bessel functions using Boost
    auto BesselJ = [](double nu, double x) { return boost::math::cyl_bessel_j(nu, x); };
    auto BesselY = [](double nu, double x) { return boost::math::cyl_bessel_y(nu, x); };

    // Calculate cm1
    double cm1 = (-BesselJ(0.5, x13) / BesselY(0.5, x13))
                 - 2 * TMath::Pi() * TMath::Cos(x13) / x13
                 - 2 * TMath::Pi() * TMath::Sin(x13) / x13;

    // Define the integrand for bm1
    auto integrand = [km3, cm1](double x) {
        double J = BesselJ(0.5, km3 * x);
        double Y = BesselY(0.5, km3 * x);
        return x * (J + cm1 * Y) * (J + cm1 * Y);
    };

    // Calculate bm1 using numerical integration
    double bm1 = TMath::Pi() * quadrature::integrate(integrand, rho1, rho2);
    double am1 = 1 / TMath::Sqrt(bm1);
          
    // Define the functions F1, F2, and Ruqayyah
    auto F1 = [am1, km3, cm1, rho1](double theta, double phi, double phip) {
        double psi1n = am1 * (BesselJ(0.5, km3 * rho1) + cm1 * BesselY(0.5, km3 * rho1)) * TMath::Cos(0.5 * phip);
        complex<double> exponent = -complex<double>(0, km3 * rho1 * (TMath::Cos(phi - phip) * TMath::Sin(theta)));
        return rho1 * psi1n * exp(exponent);
    };       
   
    auto F2 = [am1, km3, cm1, rho2](double theta, double phi, double phip) {
        double psi1n = am1 * (BesselJ(0.5, km3 * rho2) + cm1 * BesselY(0.5, km3 * rho2)) * TMath::Cos(0.5 * phip);
        complex<double> exponent = -complex<double>(0, km3 * rho2 * (TMath::Cos(phi - phip) * TMath::Sin(theta)));
        return rho2 * psi1n * exp(exponent);
    }; 
 
    auto Ruqayyah = [am1, km3, cm1](double theta, double phi, double rho) {
        double psi1np = am1 * (BesselJ(0.5, km3 * rho) + cm1 * BesselY(0.5, km3 * rho)) * TMath::Cos(0.5 * (TMath::Pi() - 0.0000001));
        complex<double> exponent = -complex<double>(0, km3 * rho * (TMath::Cos(phi - TMath::Pi() + 0.0000001) * TMath::Sin(theta)));
        return rho * psi1np * exp(exponent);
    };

    // Create a 3D histogram
    TH3F *hist = new TH3F("hist", "3D plot", 100, 0, TMath::Pi(), 100, 0, 2 * TMath::Pi(), 100, 0, 2 * TMath::Pi());

    for (int i = 0; i < 100; ++i) {
        double theta = i * TMath::Pi() / 100;
        for (int j = 0; j < 100; ++j) {
            double phi = j * 2 * TMath::Pi() / 100;
            double phip = 0; // Example value
            double rho = rho1; // Example value

            // Integrate F1, F2, and Ruqayyah over phip and rho
            auto integral_F1 = [=]() { return quadrature::integrate([=](double phip) { return F1(theta, phi, phip); }, 0, 2 * TMath::Pi()); };
            auto integral_F2 = [=]() { return quadrature::integrate([=](double phip) { return F2(theta, phi, phip); }, 0, 2 * TMath::Pi()); };
            auto integral_Ruqayyah = [=]() { return quadrature::integrate([=](double rho) { return Ruqayyah(theta, phi, rho); }, rho1, rho2); };

            double value = TMath::Sin(theta) * TMath::Sin(theta) *
                           pow(abs(integral_F1() - integral_F2() + 2 * integral_Ruqayyah()), 2);

            hist->SetBinContent(i + 1, j + 1, value);
        }
    }

    TCanvas *c1 = new TCanvas("c1", "3D Plot", 800, 600);
    hist->Draw("LEGO2");
    hist->SaveAs("LEGO2.png");
}
