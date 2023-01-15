# This script converts all rasters in a geodatabase to land surface temperature (fahrenheit) and is designed for Landsat thermal bands.

import arcpy

arcpy.env.workspace = 'C:/geodatabase.gdb'
arcpy.env.snapRaster = 'C:/geodatabase.gdb/raster.tif'

rasterList = arcpy.ListRasters()

for i in rasterList:
    output_raster = arcpy.sa.RasterCalculator([i],['x'],'(((0.00341802*x+149.0)-273.15)*(9.0/5.0))+32')
    output_raster.save('LST_{}'.format(i[4:]))

print('Completed...')
