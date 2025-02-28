#!/bin/bash

#SBATCH --job-name=reco_only        # Job name
#SBATCH --nodes=1                   # Run on 1 node
#SBATCH --ntasks=1                  # Run on 1 CPU
#SBATCH --mem=2gb                   # Job memory request
#SBATCH --time=24:00:00             # Time limit hrs:min:sec
#SBATCH --output=reco_%j.log        # Standard output and error log

# Define paths relative to the build directory
DATA_DIR=../../../Datat_Muu/onebar  # Relative path from build/ to Data_Mu

# Loop over all data directories in Data_Mu
for DATA in "$DATA_DIR"/rotz_*; do
    # Extract the numerical index from the folder name
    i=${DATA##*/rotz_}  # Extract number after "data_"

    # Compute rotation value
    VAL=$(bc <<< "scale=3; $i*0.0001")

    echo "Processing $DATA with rotz = $VAL"

    # Run the last two commands using the local eicdirc in build/
    ./eicdirc -r 2 -i "$DATA/sim.root" -u "$DATA/lut.avr.root" -o "$DATA/reco.root" \
              -trackingres 0.0005 -timeres 0.1 -timecut 0.2 -e 20000 -v 2 -rotz "$VAL"

    ./eicdirc -r 2 -i "$DATA/sim.root" -u "$DATA/lut.avr.root" -o "$DATA/reco.root" \
              -trackingres 0.0005 -timeres 0.1 -timecut 0.2 -e 20000 -v 2 -rotz "$VAL"
done

echo "All data processed successfully."
