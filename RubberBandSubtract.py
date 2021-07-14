import numpy as np
from scipy.spatial import ConvexHull


# Inputs
#   X and Y spectral data in a list or ndarray of same shape and size
#   X is the x axis values (ie. for Raman, this would be the wavenumbers on the x axis)
#   Y are the y values for each x
#   *Points is an additional argument in which you can add an array of values that correspond to locations on the x axis in which you would like to add points for the
#   linear interpolation. This may help to drop the baseline in areas that the ConvexHull algorithm misses
#
# Outputs
#   Function is implemented like this:
#   ysubtracted = y - rubberband(x, y, *[points])

def rubberband(x, y, *points):

    # Use ConvexHull to find vertices of spectra that indicate convexity
    v = ConvexHull(np.array(list(zip(x, y))), incremental=True).vertices
    
    # Roll vertices until they start from the lowest one
    v = np.roll(v, -v.argmin())

    # Leave only the ascending part
    v = v[:v.argmax()]

    # Optional points can be added to further drop the baseline
    if points:
        points = np.sort(np.reshape(points, (np.size(points), 1)))
        #initialize array for storing the indexed points to add to the rubberband baseline
        pointarray = [0]
        
        for val in points:
            xIndex = (np.abs(x - val)).argmin()
            pointarray = np.append(pointarray, xIndex)
            
        pointarray = np.delete(pointarray, (0))
        #initialize array of indexed spectral locations for rubberband baseline to drop
        insertLocs = [0]

        for val in pointarray:
            vIndex = (np.abs(v - val)).argmin()
            if v[vIndex] > val:
                insertLocs = np.append(insertLocs, vIndex)
            else:
                insertLocs = np.append(insertLocs, vIndex+1)

        insertLocs = np.delete(insertLocs, (0))
        
        #adds additional points for linear interpolation
        for count, number in enumerate(pointarray):
            v = np.insert(v, insertLocs[count], number)
            
    # Create baseline using linear interpolation between vertices
    return np.interp(x, x[v], y[v])
