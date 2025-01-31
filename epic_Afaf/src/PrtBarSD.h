#ifndef PrtBarSD_h
#define PrtBarSD_h 1

#include <vector>
#include "G4VSensitiveDetector.hh"
#include "G4AutoLock.hh"
#include <fstream>
#include "PrtBarHit.h"

class G4Step;
class G4HCofThisEvent;

class PrtBarSD : public G4VSensitiveDetector {
 public:
  PrtBarSD(const G4String &name, const G4String &hitsCollectionName, G4int nofCells);
  virtual ~PrtBarSD();

  // methods from base class
  virtual void Initialize(G4HCofThisEvent *hitCollection);
  virtual G4bool ProcessHits(G4Step *step, G4TouchableHistory *history);
  virtual void EndOfEvent(G4HCofThisEvent *hitCollection);

  // Added declaration for write_presigma_file
  void write_presigma_file(std::ofstream &presigma_file, std::ofstream &metric_file);
  void write_constraint_file(std::ofstream &constraint_file, std::ofstream &debug_con, bool debugBool);
   void write_steering_file(std::ofstream &steering_file, std::ofstream &metric_file);
 private:
  PrtBarHitsCollection *fHitsCollection;
  static G4Mutex fMutex;
  // Declare vectors as member variables
  std::vector<float> zRecon;
  std::vector<float> xRecon;
  std::vector<float> yRecon;
  
};

#endif
