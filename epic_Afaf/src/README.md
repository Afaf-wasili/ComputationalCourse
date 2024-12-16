
This project provides tools for simulating and reconstructing:

-bindices: Specify the indices of bars to misalign as a comma-separated list (e.g., -bindices "1,2,5"). This option allows you to misalign multiple bars simultaneously or select one bar
-segmentindices: Specify the indices of segments to misalign for the selected bars. Segments are indexed from 0 (default: all segments are misaligned). Example: 
segmentindices "0,1" will apply misalignments only to segments 0 and 1 of the specified bars.

-xrot, -yrot, -zrot: Rotation angles (in radians) around the X, Y, and Z axes, respectively. Used to rotate bars or segments. Example: -xrot 0.1 -yrot 0.0 -zrot 0.2.
-xshift, -yshift, -zshift: Translation shifts (in millimeters) along the X, Y, and Z axes. Used to displace bars or segments. Example: -xshift 5.0 -yshift 0.0 -zshift -3.0.

Both -bindices and -segmentindices work together. If -segmentindices is not specified, misalignments will apply to all segments of the specified bars.
Default values for shifts and rotations are 0.0, meaning no misalignment.


The script simrecbarseg.sh automates the simulation and reconstruction processes for a group of bars or individual bars with configurable misalignment settings.
example: ./eicdirc -bindices "5" -segmentindices "0,1" -zshift 5.0 -e 2
example: ./eicdirc -bindices "5,2" -segmentindices "0,1" -zshift 5.0 -e 2

