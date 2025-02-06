base) afafwasili@afafwasili-VirtualBox:~/nominalFEPIC/eicdirc/srcnew$ cat PrtBarSD.cxx 
#include "PrtBarSD.h"
#include "G4HCofThisEvent.hh"
#include "G4Step.hh"
#include "G4ThreeVector.hh"
#include "G4SDManager.hh"
#include "G4ios.hh"
#include "G4RunManager.hh"
#include "G4TransportationManager.hh"
#include <TVector3.h>
#include <cmath>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <set>

#include "/home/afafwasili/nominalFEPIC/MillepedeII/Mille.h"
#include "PrtEvent.h"
#include "PrtRunAction.h"
#include "PrtManager.h"

Mille* mille = new Mille("milleBinaryFile.bin", true); // Use the correct constructor
constexpr int misaligned_bar = 5;
constexpr double x_shift = 0.1;
constexpr double z_shift = 0.9;
constexpr double z_rotation = 0.7;

// Initialize static mutex
G4Mutex PrtBarSD::fMutex = G4MUTEX_INITIALIZER;

PrtBarSD::PrtBarSD(const G4String& name, const G4String& hitsCollectionName, G4int nofCells)
  : G4VSensitiveDetector(name) {

  G4AutoLock tuberier(&fMutex); // Lock mutex for thread safety
  collectionName.insert(hitsCollectionName);

  // Open files
  constraint_file.open("Tracker_con.txt");
  presigma_file.open("Tracker_par.txt");
  steering_file.open("Tracker_steering.txt");
  metric_file.open("metric_log.txt");

  // Write headers
  constraint_file << "* Constraints\n";
  presigma_file << "Parameter   InitialValue   PreSigma\n";

  // Generate alignment files
  write_constraint_file();
  write_presigma_file();
  write_steering_file();
}

PrtBarSD::~PrtBarSD() {
  mille->end();
  delete mille;

  // Close files
  constraint_file.close();
  presigma_file.close();
  steering_file.close();
  metric_file.close();
}

void PrtBarSD::Initialize(G4HCofThisEvent* hce) {
  fHitsCollection = new G4THitsCollection<PrtBarHit>(SensitiveDetectorName, collectionName[0]);
  G4int hcID = G4SDManager::GetSDMpointer()->GetCollectionID(collectionName[0]);
  hce->AddHitsCollection(hcID, fHitsCollection);

  // Clear temporary hits for new event
  fTempHits.clear();
}

void PrtBarSD::write_constraint_file() {
  for(int bar_id=0; bar_id<10; bar_id++) {
    if(bar_id == misaligned_bar) continue;
    constraint_file << "Constraint 0.0\n";
    constraint_file << bar_id+1 << " 1.0\n";
  }
}

void PrtBarSD::write_presigma_file() {
  for(int bar_id=0; bar_id<10; bar_id++) {
    for(int param=0; param<6; param++) {
      double presigma = -1.0;
      if(bar_id == misaligned_bar) {
        if(param == 0 || param == 2 || param == 5) presigma = 0.5;
      }
      presigma_file << bar_id*10 + param + 1 << " " 
                   << 0.0 << " " << presigma << "\n";
    }
  }
}

void PrtBarSD::write_steering_file() {
  steering_file << "* g-2 Tracker Alignment\n"
                << "method inversion 5 0.01\n"
                << "printrecord 2\n"
                << "Tracker_con.txt\n"
                << "Tracker_par.txt\n"
                << "end\n";
}

G4bool PrtBarSD::ProcessHits(G4Step* step, G4TouchableHistory* hist) {
  G4Track* track = step->GetTrack();
  if(track->GetParentID() > 0) return true; // Only primary particles

  G4String ParticleName = track->GetDynamicParticle()->GetParticleDefinition()->GetParticleName();
  if (ParticleName == "opticalphoton") return true; // Skip optical photons

  G4StepPoint* pstep = step->GetPostStepPoint();
  G4ThreeVector nominal_pos = pstep->GetPosition();
  G4ThreeVector gpos = nominal_pos;

  G4TouchableHistory* touchable = (G4TouchableHistory*)(pstep->GetTouchable());
  G4int bar_id = touchable->GetCopyNumber(1); // Get the bar ID

  // Apply misalignment to the specified bar
  if(bar_id == misaligned_bar) {
    double x = nominal_pos.x() * cos(z_rotation) - nominal_pos.y() * sin(z_rotation);
    double y = nominal_pos.x() * sin(z_rotation) + nominal_pos.y() * cos(z_rotation);
    gpos.setX(x + x_shift);
    gpos.setZ(nominal_pos.z() + z_shift);
  }

  // Store hit data for regression
  HitData hit;
  hit.pos = gpos; // Misaligned position
  hit.nominal_pos = nominal_pos; // Original position
  hit.bar_id = bar_id;
  fTempHits.push_back(hit);

  // Create and store hit in collection
  PrtBarHit* newHit = new PrtBarHit();
  newHit->SetTrackID(track->GetTrackID());
  newHit->SetPos(gpos);
  newHit->SetMom(track->GetMomentum());
  fHitsCollection->insert(newHit);

  return true;
}
void PrtBarSD::EndOfEvent(G4HCofThisEvent*) {
  if (fTempHits.size() < 2) return; // Need at least 2 points for meaningful residuals

  // Linear regression in X-Z plane
  double S = 0.0, Sz = 0.0, Sx = 0.0, Szz = 0.0, Sxz = 0.0;
  const double sigmaHit = 0.01; // Position measurement uncertainty (1 mm)
  const double err2 = sigmaHit * sigmaHit;

  // First pass: calculate sums for regression
  for (const auto& hit : fTempHits) {
    const double z = hit.pos.z();
    const double x = hit.pos.x();
    
    S += 1.0 / err2;
    Sz += z / err2;
    Sx += x / err2;
    Szz += z*z / err2;
    Sxz += x*z / err2;
  }

  const double denom = S * Szz - Sz * Sz;
  if (denom == 0) return; // Avoid division by zero

  // Calculate track parameters
  const double slope = (S * Sxz - Sz * Sx) / denom;
  const double intercept = (Sx * Szz - Sz * Sxz) / denom;

  // Second pass: calculate residuals and derivatives
  for (const auto& hit : fTempHits) {
    const double z = hit.pos.z();
    const double x = hit.pos.x();
    const double residual = x - (intercept + slope * z);
    
    // Local derivatives (track parameters)
    float derLc[2] = {1.0f, static_cast<float>(z)}; // d(residual)/d(intercept), d(residual)/d(slope)
    
    // Global derivatives (alignment parameters)
    float derGl[3] = {
      1.0f,                         // d(residual)/dΔx
      -static_cast<float>(slope),   // d(residual)/dΔz (chain rule through slope)
      -static_cast<float>(hit.nominal_pos.x()) // d(residual)/dθz (rotation)
    };

    // Parameter labels (1-based indices)
    int labels[3] = {
      hit.bar_id * 10 + 1,  // Δx (parameter 1 for this bar)
      hit.bar_id * 10 + 3,  // Δz (parameter 3 for this bar)
      hit.bar_id * 10 + 6   // θz (parameter 6 for this bar)
    };

    // Only add misaligned bar to Millepede (others are reference)
    if (hit.bar_id == misaligned_bar) {
      mille->mille(
        2,        // Number of local parameters
        derLc,    // Local derivatives array
        3,        // Number of global parameters
        derGl,    // Global derivatives array
        labels,   // Global parameter labels
        static_cast<float>(residual), 
        static_cast<float>(sigmaHit)
      );
    }
  }

  fTempHits.clear(); // Clear hits for next event

  // No need to manually flush - Millepede handles buffering internally
  // Data will be written when mille->end() is called in destructor
}
