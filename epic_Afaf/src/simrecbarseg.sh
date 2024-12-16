#!/bin/bash

cd build || { echo "Build directory not found! Exiting."; exit 1; }

cmake ../ -DWITH_GEANT4_UIVIS=OFF
make -j4

OUTPUT_DIR="../data1"
RECO_DIR="$OUTPUT_DIR/reco"
mkdir -p "$OUTPUT_DIR" "$RECO_DIR"

START_BAR=0
END_BAR=1

ROTATION_Z_VALUES=(1.75)
ROTATION_X_VALUES=(1.0)
ROTATION_Y_VALUES=(1.0)
Z_SHIFT_VALUES=(10.0)
X_SHIFT_VALUES=(5.0)
Y_SHIFT_VALUES=(5.0)
SEGMENT_INDICES="0,1,2,3"  # Define all segments for each bar
EVENTS=20

for BAR_INDEX in $(seq $START_BAR $END_BAR); do
    for ROTATION_Z in "${ROTATION_Z_VALUES[@]}"; do
        for ROTATION_X in "${ROTATION_X_VALUES[@]}"; do
            for ROTATION_Y in "${ROTATION_Y_VALUES[@]}"; do
                for Z_SHIFT in "${Z_SHIFT_VALUES[@]}"; do
                    for X_SHIFT in "${X_SHIFT_VALUES[@]}"; do
                        for Y_SHIFT in "${Y_SHIFT_VALUES[@]}"; do
                            SIM_FILE="$OUTPUT_DIR/sim_bar${BAR_INDEX}_segments_all_rotX${ROTATION_X}_rotY${ROTATION_Y}_rotZ${ROTATION_Z}_z${Z_SHIFT}_x${X_SHIFT}_y${Y_SHIFT}.root"
                            RECO_FILE="$RECO_DIR/reco_bar${BAR_INDEX}_segments_all_rotX${ROTATION_X}_rotY${ROTATION_Y}_rotZ${ROTATION_Z}_z${Z_SHIFT}_x${X_SHIFT}_y${Y_SHIFT}.root"

                            ./eicdirc -b 1 -bindices "$BAR_INDEX" -segmentindices "$SEGMENT_INDICES" -r 0 -o "$SIM_FILE" -e "$EVENTS" -theta 30 -x "mix_pik" -p 6 -w 0 -g 1 -c 2031 -l 3 -trackingres 0.0005 \
                                      -xrot "$ROTATION_X" -yrot "$ROTATION_Y" -zrot "$ROTATION_Z" -zshift "$Z_SHIFT" -xshift "$X_SHIFT" -yshift "$Y_SHIFT"
                            if [ $? -ne 0 ]; then
                                echo "Simulation failed for BarIndex = $BAR_INDEX with all segments. Skipping."
                                continue
                            fi

                            ./eicdirc -b 1 -r 2 -i "$SIM_FILE" -u lut.avr.root -o "$RECO_FILE" -trackingres 0.0005 -timeres 0.1 -timecut 0.2 -e "$EVENTS" -v 2
                            if [ $? -ne 0 ]; then
                                echo "Reconstruction failed for BarIndex = $BAR_INDEX with all segments. Skipping."
                                continue
                            fi

                            for FILE in "$RECO_DIR"/*.png; do
                                if [[ -f "$FILE" && "$FILE" != *"_bar"* ]]; then
                                    BASENAME=$(basename "$FILE" .png)
                                    mv "$FILE" "$RECO_DIR/${BASENAME}_bar${BAR_INDEX}_segments_all_rotX${ROTATION_X}_rotY${ROTATION_Y}_rotZ${ROTATION_Z}_z${Z_SHIFT}_x${X_SHIFT}_y${Y_SHIFT}.png"
                                fi
                            done
                        done
                    done
                done
            done
        done
    done
done
