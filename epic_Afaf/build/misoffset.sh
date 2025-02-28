#!/bin/bash                                                                                                    

#SBATCH --job-name=reco_only        # Job name                                                                
#SBATCH --nodes=1                   # Run on 1 node                                                           
#SBATCH --ntasks=1                  # Run on 1 CPU                                                            
#SBATCH --mem=2gb                   # Job memory request                                                      
#SBATCH --time=24:00:00             # Time limit hrs:min:sec                                                  
#SBATCH --output=reco_%j.log        # Standard output and error log                                           

# Define correct data directory (Fixing typo from "Datat_Muu" to "Data_Mu")
DATA_DIR=~/Datat_Muu/onebarlens  # Make sure this path exists!

# Debug: Check directory exists                                                                                
if [[ ! -d "$DATA_DIR" ]]; then
    echo "Error: Data directory $DATA_DIR does not exist!" | tee -a script_log.txt
    exit 1
fi

# Logging function
log_file="shiftx_reco_log.txt"
echo "Logging script execution to $log_file"
echo "Started processing at $(date)" > "$log_file"

# Loop over all valid data directories                                                                        
for DATA in "$DATA_DIR"/shiftx_*; do
    # Extract numerical index from folder name                                                                
    i=${DATA##*/shiftx_}  # Get number after "shifty_"                                                             

    # Compute shift value                                                                                   
    VAL=$(bc <<< "scale=3; ${1:-0}*0.001")  # Default to 0 if $1 is empty                                       

    echo "Processing $DATA with shifty = $VAL" | tee -a "$log_file"

    # Ensure required input files exist                                                                        
    if [[ ! -f "$DATA/sim.root" || ! -f "$DATA/lut.avr.root" ]]; then
        echo "Warning: Missing sim.root or lut.avr.root in $DATA, skipping..." | tee -a "$log_file"
        continue
    fi

    # Run the command and log output                                                                                          
    ./eicdirc -r 2 -i "$DATA/sim.root" -u "$DATA/lut.avr.root" -o "$DATA/reco.root" \
              -trackingres 0.0005 -timeres 0.1 -timecut 0.2 -e 20000 -v 2 -shiftx "$VAL" \
              2>&1 | tee -a "$log_file"

    # Check if reco.root was created successfully
    if [[ ! -f "$DATA/reco.root" ]]; then
        echo "Error: reco.root not created for $DATA" | tee -a "$log_file"
        continue
    fi

    echo "Finished processing $DATA" | tee -a "$log_file"
done

echo "All data processed successfully at $(date)" | tee -a "$log_file"


