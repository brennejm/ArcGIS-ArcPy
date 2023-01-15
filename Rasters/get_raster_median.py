# This script finds all rasters in a geodatabase and prints out the median value for all raster cells.

import arcpy
import numpy as np

arcpy.env.workspace = 'C:/geodatabase.gdb'

for raster in arcpy.ListRasters():
    arr = arcpy.RasterToNumPyArray(in_raster=raster)
    print('{}: {}'.format(raster,np.median(arr)))
