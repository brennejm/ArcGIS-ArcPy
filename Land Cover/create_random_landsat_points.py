# ArcGIS Pro 3.0 and Python 3.7.10
# This script takes in a landsat raster and an area of interest (aoi)
# and based on user inputs creates n random points within the aoi
# with coordinates exactly at landsat raster cell centers. This script
# is designed to be used in creating training datasets for image
# classification.

import arcpy
from arcpy.sa import *

## UPDATE AS NEEDED IN THIS SECTION ##

# Number of random points to create
n = 100

# Internal buffer from aoi edge for random points (meters)
b = -240

# Closest distance random points can be to one another (meters)
d = 120

# Update the folder or geodatabase path and shapefile or feature class AOI names
directory = 'C:/geodatabase.gdb'
aoi = 'AreaOfInterest'

# Update the raster path
landsatRaster = Raster('C:/raster.tif')

# Update the name of the output shapefile or feature class
newPoints = 'raster_cell_points'

## DO NOT UPDATE BEYOND THIS LINE ##

# Leave these names unchanged
aoiBuffer = 'in_memory/aoiBuffer'
randPoints = 'in_memory/randPoints'

# Get landsat raster min x and y extent
xmin = int(landsatRaster.extent.XMin)
ymin = int(landsatRaster.extent.YMin)

# Set the output projection to the same as the input raster
rasterProjection = arcpy.Describe(landsatRaster).spatialReference
arcpy.env.outputCoordinateSystem = rasterProjection

# Create negative buffer to use in random point creation
# to ensure the nearest raster cell to each random point
# will fall within area of interest
arcpy.analysis.Buffer('{}/{}'.format(directory,aoi), aoiBuffer, '{} Meters'.format(str(b)))

# Create random points within the aoiBuffer
arcpy.management.CreateRandomPoints('in_memory', 'randPoints', aoiBuffer, '', n, '{} Meters'.format(str(d)), 'POINT')

# Save new coordinates
coords = []

# Iterate through random points and get coordinates
with arcpy.da.SearchCursor(randPoints, ['SHAPE@XY']) as cursor:
    for row in cursor:
        lon = int(round(row[0][0],0))
        lat = int(round(row[0][1],0))

        # Correct random point coords to nearby raster pixel center
        newLon = (lon + (30 - ((lon - xmin) % 30))) + 15
        newLat = (lat + (30 - ((lat - ymin) % 30))) + 15

        # Append coords to list
        # Must have trailing comma according to link: https://support.esri.com/en/technical-article/000011654
        coords.append(((newLon,newLat),))

# Create new feature class
arcpy.CreateFeatureclass_management(directory,newPoints,'POINT')

# Create insert cursor
cursor = arcpy.da.InsertCursor('{}/{}'.format(directory,newPoints), ['SHAPE@XY'])

#Iterate through coords and enter new points
for i in coords:
    cursor.insertRow(i)

# Delete cursor object
del cursor
