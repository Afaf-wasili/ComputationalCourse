$ cat PrtBarSD.cxx 
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

// Include Mille header
#include "/home/afafwasili/nominalFEPIC/MillepedeII/Mille.h"

#include "PrtEvent.h"
#include "PrtRunAction.h"
#include "PrtManager.h"

// Initialize Mille with the binary file
static Mille* mille("milleBinaryFile.bin");
// Constraints, Steering and Parameter files are the inputs to Pede (together with binary file).
std::ofstream constraint_file("Tracker_con.txt");
std::ofstream presigma_file("Tracker_par.txt");
std::ofstream metric_file("metric_log.txt");
std::ofstream steering_file("Tracker_steering.txt");

// Define the static mutex
G4Mutex PrtBarSD::fMutex = G4MUTEX_INITIALIZER;

PrtBarSD::PrtBarSD(const G4String &name, const G4String &hitsCollectionName, G4int nofCells)
  : G4VSensitiveDetector(name), fHitsCollection(NULL) {

  G4AutoLock tuberier(&fMutex);
  collectionName.insert(hitsCollectionName);
}

PrtBarSD::~PrtBarSD() {
  delete mille;
}

void PrtBarSD::Initialize(G4HCofThisEvent *hce) {
  fHitsCollection = new PrtBarHitsCollection(SensitiveDetectorName, collectionName[0]);
  G4int hcID = G4SDManager::GetSDMpointer()->GetCollectionID(collectionName[0]);
  hce->AddHitsCollection(hcID, fHitsCollection);
}

// ** Constraint File Generation **
void PrtBarSD::write_constraint_file(std::ofstream& constraint_file, std::ofstream& debug_con, bool debugBool) {
    if (!constraint_file.is_open()) {
        G4cerr << "Error: Constraint file not open!" << G4endl;
        return;
    }

    int barN = 10;  // Total bars (0-9)
    float one = 1.0; // Constraint weight
    std::stringstream labelStream;

    G4cout << "Writing constraint file..." << G4endl;

    // Constrain the first and last bars
    for (int barIndex : {0, 9}) { 
        constraint_file << "Constraint 0.0\n";
        for (int param = 0; param < 3; param++) { // X-shift, Y-shift, X-rotation
            int label = (barIndex * 100) + param + 1;
            constraint_file << label << " " << std::fixed << std::setprecision(5) << one << "\n";
            labelStream << label << "; ";
        }
    }

    G4cout << "Constraint file written successfully." << G4endl;
}

// ** Presigma File Generation **
void PrtBarSD::write_presigma_file(std::ofstream &presigma_file, std::ofstream &metric_file) {
    if (!presigma_file.is_open()) {
        G4cerr << "Error: Presigma file not open!" << G4endl;
        return;
    }

    presigma_file << "PARAMETERS\n";
    metric_file << " | P: ";

    int barN = 10;
    int misalignedBar = 5; // Only bar 5 is misaligned

    for (int i = 0; i < barN; i++) {
        for (int param = 0; param < 3; param++) { // X-shift, Y-shift, X-rotation
            float initialValue = (i == misalignedBar) ? ((param == 0) ? -0.1 : (param == 1) ? 0.4 : 0.5) : 0.0;
            float preSigma = (i == misalignedBar) ? 0.01 : -1.0;
            int label = (i * 100) + param + 1;
            presigma_file << label << " " << std::fixed << std::setprecision(5) << initialValue
                          << " " << preSigma << "\n";
            metric_file << label << " " << initialValue << " " << preSigma << "; ";
        }
    }

    G4cout << "Presigma file written successfully." << G4endl;
}

// ** Steering File Generation **
void PrtBarSD::write_steering_file(std::ofstream &steering_file, std::ofstream &metric_file) {
    if (steering_file.is_open()) {
        std::stringstream pede_method; 
        pede_method.str(""); 
        pede_method << "method inversion 5 0.001";
        metric_file << "| " << pede_method.str().c_str();

        steering_file << "* g-2 Tracker Alignment: PEDE Steering File" << std::endl
                      << " " << std::endl
                      << "Tracker_con.txt   ! constraints text file (if applicable) " << std::endl
                      << "Tracker_par.txt   ! parameters (presgima) text file (if applicable)" << std::endl
                      << "Cfiles ! following bin files are Cfiles" << std::endl
                      << "Tracker_data.bin   ! binary data file" << std::endl
                      << "method inversion 5 0.001" << std::endl
                      << "printrecord 2 -1 ! produces mpdebug.txt for record 2 with the largest value of χ2/Ndf" << std::endl
                      << " " << std::endl
                      << "end ! optional for end-of-data" << std::endl;
    }
}

G4bool PrtBarSD::ProcessHits(G4Step *step, G4TouchableHistory *hist) {

  // energy deposit
  G4Track *track = step->GetTrack();
  int parentId = track->GetParentID();
  if (parentId > 0) return true; // only primaries

  G4String ParticleName = track->GetDynamicParticle()->GetParticleDefinition()->GetParticleName();
  if (ParticleName == "opticalphoton") return true;

  PrtBarHit *newHit = new PrtBarHit();
  newHit->SetTrackID(step->GetTrack()->GetTrackID());
  newHit->SetPos(step->GetPostStepPoint()->GetPosition());
  newHit->SetMom(track->GetMomentum());

  auto pstep = step->GetPostStepPoint();
  G4ThreeVector gpos = pstep->GetPosition();
  G4ThreeVector gmom = pstep->GetMomentum();
  G4TouchableHistory *touchable = (G4TouchableHistory *)(pstep->GetTouchable());
  G4ThreeVector lpos = touchable->GetHistory()->GetTransform(1).TransformPoint(gpos);

  if (fHitsCollection->entries() == 0) {
    PrtManager::Instance()->getEvent()->setMomentumBefore(TVector3(gmom.x(), gmom.y(), gmom.z()));
    PrtManager::Instance()->getEvent()->setPosition(TVector3(lpos.x(), lpos.y(), lpos.z()));
  } else {    
    PrtManager::Instance()->getEvent()->setMomentumAfter(TVector3(gmom.x(), gmom.y(), gmom.z()));
    PrtManager::Instance()->getEvent()->setPositionAfter(TVector3(lpos.x(), lpos.y(), lpos.z()));
  }

  // Collect hits
  static std::vector<float> zRecon;
  static std::vector<float> xRecon;
  static std::vector<float> yRecon;
  zRecon.push_back(lpos.z());
  xRecon.push_back(lpos.x());
  yRecon.push_back(lpos.y());

  if (zRecon.size() < 2) {
    fHitsCollection->insert(newHit);
    return true; // Not enough data points for regression yet
  }

  // Perform regression to calculate slope and intercept
  float S = 0, Sz = 0, Su = 0, Szz = 0, Suz = 0, Sy = 0;
  float err2 = 0.01 * 0.01;

  for (size_t i = 0; i < zRecon.size(); i++) {
      S += 1 / err2;
      Sz += zRecon[i] / err2;
      Su += xRecon[i] / err2;
      Sy += yRecon[i] / err2;
      Szz += zRecon[i] * zRecon[i] / err2;
      Suz += xRecon[i] * zRecon[i] / err2;
  }

  float denominator = (S * Szz - Sz * Sz);
  if (denominator == 0) {
      G4cerr << "Error: Zero denominator in regression calculation!" << G4endl;
      return false;
  }

  float slopeX = (S * Suz - Sz * Su) / denominator;
  float interceptX = (Su * Szz - Sz * Suz) / denominator;

  // Calculate slope and intercept for y
  float slopeY = (S * Sy - Sz * Sy) / denominator;
  float interceptY = (Su * Sy - Sz * Sy) / denominator;

  float z = lpos.z();
  float x = lpos.x();
  float y = lpos.y();
  float mX = slopeX;
  float cX = interceptX;
  float mY = slopeY;
  float cY = interceptY;
  float zc = 0;
  float xc = 0;
  float yc = 0;

  // Labels based on hit count
  int hitCount = fHitsCollection->entries();
  int l1 = hitCount + 1;
  int l2 = hitCount + 2;
  int l3 = hitCount + 3;
  int label[] = {l1, l2, l3};

  // Local derivatives: see alignment.tex for derivations
  float dlc1 = (cX + mX * z - x) / (sqrt(mX * mX + 1) * abs(cX + mX * z - x)); // "DCA magnitude" dR/dc
  float dlc2 = ((mX * z - x) * abs(cX + mX * z - x)) / (pow(mX * mX + 1, 1.5) * abs(cX + mX * z - x)); // dR/dm
  float derlc[] = {dlc1, dlc2};
  // Global derivatives
  float dgl1 = (cX + mX * z - x) / (sqrt(mX * mX + 1) * abs(cX + mX * z - x)); // dR/dx
  float dgl2 = (mX * (cX + mX * z - x)) / (sqrt(mX * mX + 1) * abs(cX + mX * z - x)); // dR/dz
  float dgl3 = ((mX * (cX + mX * z - x)) / (sqrt(mX * mX + 1) * abs(cX + mX * z - x)) * (-x + xc)) + ((cX + mX * z - x) / (sqrt(mX * mX + 1) * abs(cX + mX * z - x)) * (z - zc)); // dR/dθ
  float dergl[] = {dgl1, dgl2, dgl3};

  const int nalc = 2;
  const int nagl = 3;
  float resiudalRecon = newHit->GetPos().x();
  float resolution = 0.1;

  mille.mille(nalc, derlc, nagl, dergl, label, resiudalRecon, resolution);

  fHitsCollection->insert(newHit);

  return true;
}

void PrtBarSD::EndOfEvent(G4HCofThisEvent *) {
    std::ofstream debug_con("debug_constraints.txt");
    write_constraint_file(constraint_file, debug_con, true);
    write_presigma_file(presigma_file, metric_file);
    write_steering_file(steering_file, metric_file);

    zRecon.clear();
    xRecon.clear();
    yRecon.clear();

    mille->end();
}
afafwasili@afafwasili-VirtualBox:~/nominalFEPIC/eicdirc/src$ 
