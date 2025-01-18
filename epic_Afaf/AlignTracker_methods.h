#ifndef ALIGNTRACKER_M
#define ALIGNTRACKER_M

/* This header file contains definitions of constant variables used in
 * the method class, as well as function declarations, and definitions of functions.
 */

///XXX some includes may be redundant
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <stdexcept>
#include <cmath>
#include <numeric>
#include <bitset>
#include <TF1.h>
#include <TMath.h>
#include <TRandom3.h> // Random number facility XXX use art random? 
#include "Logger.hh"

/**
   Structure to contain data of a generated track, with the number of hits, their positions, the uncertainty in the positions, and the plane number hit.
*/
struct MCData {
    int totalPhotonHits; /** Number of photon hits in the detector */
    // *** Hit Parameters *** // 
    std::vector<float> residualsRecon; // Reconstruction residuals between the fitted track and detected position 
    std::vector<float> residualsTruth; // Truth residuals
    std::vector<int> barID; // Bar ID for reconstruction
    std::vector<int> lensID; // Lens ID for photon path
    std::vector<int> prismID; // Prism ID for photon path
    std::vector<int> sensorID; // Sensor ID for detection
    std::vector<float> hitTime; // Photon hit time
    std::vector<float> hitWavelength; // Photon hit wavelength
    std::vector<float> xBar; // X position of bar
    std::vector<float> zBar; // Z position of bar
    std::vector<float> xLens; // X position of lens
    std::vector<float> zLens; // Z position of lens
    std::vector<float> xPrism; // X position of prism
    std::vector<float> zPrism; // Z position of prism
    std::vector<float> xSensor; // X position of sensor
    std::vector<float> zSensor; // Z position of sensor
    // ** Track parameters ** //
    float x0; // Entrance of beam in x
    float x1; // Exit position
    float slopeTruth; 
    float interceptTruth;
    float slopeRecon;
    float interceptRecon;
    float pValue;
    float chi2Circle;
    bool cut = false; // Cut trigger to kill the track
};

// Define and return the center of rotational symmetry
struct RotationCentres {
    std::vector<float> zCentres;
    std::vector<float> xCentres;
};

/**
   Singleton class to represent the DIRC detector geometry, including bars, lenses, prisms, and sensors.
*/
class DIRCTracker {

private:

    static DIRCTracker* s_instance; // Pointer to instance of class
    int photonCount; // Number of photons to be simulated passing through the detector

    // Random number generator for simulation
    int randomSeed = 1234;
    TRandom3* randomFacility = new TRandom3(randomSeed);

    // **** Counters ****
    int rejectedPhotons = 0; // Rejected photons due to geometry constraints
    bool cutTriggered; // Set to false at each photon generation, triggered if smeared position exceeds limits

    // **** Detector Constants ****
    static const int barCount = 12; // Number of bars
    static const int lensCount = 4; // Number of lenses
    static const int prismCount = 2; // Number of prisms
    static const int sensorCount = 16; // Number of sensors
    static constexpr float barLength = 490.0; // Length of each bar (cm)
    static constexpr float barWidth = 3.5; // Width of each bar (cm)
    static constexpr float barThickness = 1.7; // Thickness of each bar (cm)
    static constexpr float lensRadius = 5.0; // Radius of the lens (cm)
    static constexpr float prismHeight = 10.0; // Height of the prism (cm)
    static constexpr float prismWidth = 3.5; // Width of the prism (cm)
    static constexpr float sensorSize = 2.0; // Size of the sensor (cm)

    // Alignment offsets for bars, lenses, prisms, and sensors
    float barOffsetsX[barCount] = {0.0};
    float barOffsetsZ[barCount] = {0.0};
    float barRotations[barCount] = {0.0}; // Rotations of bars (in radians)
    float lensOffsetsX[lensCount] = {0.0};
    float lensOffsetsZ[lensCount] = {0.0};
    float prismOffsetsX[prismCount] = {0.0};
    float prismOffsetsZ[prismCount] = {0.0};
    float sensorOffsetsX[sensorCount] = {0.0};
    float sensorOffsetsZ[sensorCount] = {0.0};

    DIRCTracker();
    ~DIRCTracker();

public:
    static DIRCTracker* instance();

    /**
       Simulates photon propagation through the detector.
       @return MCData structure with event data.
    */
    MCData processEvent();

    /**
       Adjusts the alignment of a bar.
       @param barIndex Index of the bar to adjust
       @param offsetX X-axis offset to apply
       @param offsetZ Z-axis offset to apply
       @param rotation Rotation angle (radians) to apply
    */
    void alignBar(int barIndex, float offsetX, float offsetZ, float rotation);

    /**
       Adjusts the alignment of a lens.
       @param lensIndex Index of the lens to adjust
       @param offsetX X-axis offset to apply
       @param offsetZ Z-axis offset to apply
    */
    void alignLens(int lensIndex, float offsetX, float offsetZ);

    /**
       Adjusts the alignment of a prism.
       @param prismIndex Index of the prism to adjust
       @param offsetX X-axis offset to apply
       @param offsetZ Z-axis offset to apply
    */
    void alignPrism(int prismIndex, float offsetX, float offsetZ);

    /**
       Adjusts the alignment of a sensor.
       @param sensorIndex Index of the sensor to adjust
       @param offsetX X-axis offset to apply
       @param offsetZ Z-axis offset to apply
    */
    void alignSensor(int sensorIndex, float offsetX, float offsetZ);

    // Getter methods
    int getBarCount() const {
        return barCount;
    }

    int getLensCount() const {
        return lensCount;
    }

    int getPrismCount() const {
        return prismCount;
    }

    int getSensorCount() const {
        return sensorCount;
    }

    float getBarLength() const {
        return barLength;
    }

    float getBarWidth() const {
        return barWidth;
    }

    float getBarThickness() const {
        return barThickness;
    }

    float getLensRadius() const {
        return lensRadius;
    }

    float getPrismHeight() const {
        return prismHeight;
    }

    float getPrismWidth() const {
        return prismWidth;
    }

    float getSensorSize() const {
        return sensorSize;
    }

    float getBarOffsetX(int barIndex) const {
        return barOffsetsX[barIndex];
    }

    float getBarOffsetZ(int barIndex) const {
        return barOffsetsZ[barIndex];
    }

    float getBarRotation(int barIndex) const {
        return barRotations[barIndex];
    }

    float getLensOffsetX(int lensIndex) const {
        return lensOffsetsX[lensIndex];
    }

    float getLensOffsetZ(int lensIndex) const {
        return lensOffsetsZ[lensIndex];
    }

    float getPrismOffsetX(int prismIndex) const {
        return prismOffsetsX[prismIndex];
    }

    float getPrismOffsetZ(int prismIndex) const {
        return prismOffsetsZ[prismIndex];
    }

    float getSensorOffsetX(int sensorIndex) const {
        return sensorOffsetsX[sensorIndex];
    }

    float getSensorOffsetZ(int sensorIndex) const {
        return sensorOffsetsZ[sensorIndex];
    }
};

#endif
