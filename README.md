# RubberBand
Rubberband Spectral Subtraction 

Particularly in Raman spectra, there is often an increasing baseline background in the spectra. This can be due to a number of phenomena such as fluorescence, 
phosphorescence, ambient light etc. The removal of these baseline effects are key for reducing quantification standard errors and driving down limits of detection.

The rubberband algorithm performs baseline subtraction by determining support points by finding the convex hull of each spectrum. The baselines are then joined together via
piecewise linear or (smoothing) splines through the support points.

