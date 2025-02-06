
#ifndef PrtDetectorConstruction_h
#define PrtDetectorConstruction_h 1

#include "globals.hh"
#include "G4Material.hh"
#include "G4VUserDetectorConstruction.hh"
#include "G4RotationMatrix.hh"
#include "G4VPhysicalVolume.hh"

#include "TChain.h"

#include "PrtRun.h"
#include "PrtDetectorConstructionMessenger.h"

class PrtDetectorConstructionMessenger;

class PrtDetectorConstruction : public G4VUserDetectorConstruction {
public:
  // Constructor with misalignment parameters
PrtDetectorConstruction(std::string barIndices = "-1",
                        std::string segmentIndices = "-1",
                        double zRotation = 0.0,
                        double xRotation = 0.0,
                        double yRotation = 0.0,
                        double zShift = 0.0,
                        double xShift = 0.0,
                        double yShift = 0.0);

  virtual ~PrtDetectorConstruction();
   virtual G4VPhysicalVolume* Construct();
  virtual void ConstructSDandField();
  void DefineMaterials();
  void SetVisualization();
  void SetRotation(G4double angle);
  void DrawHitBox(G4int id);
  void SetLens(G4int id);
  void SetQuantumEfficiency(G4int id);

private:
void LogMisalignments(std::ofstream& logFile, int barIndex, double xShift, double yShift,
                      double zShift, double xRotation, double yRotation, double zRotation);

  PrtRun *fRun;

  // Logical volumes
  G4LogicalVolume *lExpHall;
  G4LogicalVolume *lFront;
  G4LogicalVolume *lDirc;
  G4LogicalVolume *lFd;
  G4LogicalVolume *lBar;
  G4LogicalVolume *lTracker;
  G4LogicalVolume *lGlue;
  G4LogicalVolume *lMirror;
  G4LogicalVolume *lLens1;
  G4LogicalVolume *lLens2;
  G4LogicalVolume *lLens3;
  G4LogicalVolume *lPrizm;
  G4LogicalVolume *lPrizmT1;
  G4LogicalVolume *lPrizmT2;
  G4LogicalVolume *lWedge;
  G4LogicalVolume *lSWedge;
  G4LogicalVolume *lBlock;
  G4LogicalVolume *lFmirror;
  G4LogicalVolume *lWindow;
  G4LogicalVolume *lMcp;
  G4LogicalVolume *lPixel;
  G4LogicalVolume *lExpVol;
  G4LogicalVolume *lGlueE;
  G4LogicalVolume *lBWindow, *lCookie;

  // Physical volumes
  G4VPhysicalVolume *wBar;
  G4VPhysicalVolume *wTracker;
  G4VPhysicalVolume *wGlue;
  G4VPhysicalVolume *wMirror;
  G4VPhysicalVolume *wDirc;

  // Materials
  G4Material *defaultMaterial; // material for bars
  G4Material *BarMaterial;     // material for bars
  G4Material *OilMaterial;
  G4Material *MirrorMaterial;  // material of mirror
  G4Material *epotekMaterial;
  G4Material *opticalCookieMaterial;
  G4Material *Nlak33aMaterial;
  G4Material *PbF2Material;
  G4Material *SapphireMaterial;
  G4Material *frontMaterial;

  // Detector configuration parameters
  int fNRow;
  int fNCol;
  int fNBoxes;
  double fRadius;
  double fNpix1;
  double fNpix2;
  double fBoxWidth;
  int fGeomType;
  int fEvType;
  int fMcpLayout;
  int fLensId;
  double fdTilt;
  double fNBar;
  double fHall[3];
  double fBar[3];
  double fMirror[3];
  double fFd[3];
  double fPrizm[4];
  double fPrizmT[6];
  double fLens[4];
  double fBWindow[3];
  double fCookie[3];
  double fMcpTotal[3];
  double fMcpActive[3];
  double fBarsGap;
  double fRotAngle;
  double *fQuantumEfficiency;
  int fRunType, fStudy, fTest1, fTest2, fTest3;

  // Misalignment parameters
  std::vector<int> fBarIndices;    // Bar indices for misalignment, passed as a string
  double fRotationX;          // Rotation about X-axis
  double fRotationY;          // Rotation about Y-axis
  double fRotationZ;          // Rotation about Z-axis
  double fXShift;             // Shift in X direction
  double fYShift;             // Shift in Y direction
  double fZShift;             // Shift in Z direction
std::vector<int> fSegmentIndices; // List of segment indices to misalign
  G4ThreeVector fPrismShift;

  G4RotationMatrix *fPrtRot;
  PrtDetectorConstructionMessenger *fGeomMessenger;

  // Activation flags for misalignment modes
  bool fActivateXShift, fActivateYShift, fActivateZShift;
  bool fActivateXRotation, fActivateYRotation, fActivateZRotation;

  // Logging and other members
};

#endif
