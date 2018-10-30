## Program: Coordinate_Format.py
## Description: Given two variables (longitude, latitude), it
## will round the coordinates, set the number of decimal
## places equal to dec, and return a string.

def coordinates(dec,lon,lat):
    
    x = str(round(float(lon),dec))
    y = str(round(float(lat),dec))

    # If any ending digits rounded to zero, pad the coordinate to equal numDec.
    if len(x[x.find('.')+1:]) < dec:
        while len(x[x.find('.')+1:]) < dec:
            x = x + '0'

    if len(y[y.find('.')+1:]) < dec:
        while len(y[y.find('.')+1:]) < dec:
            y = y + '0'
            
    return '{}, {}'.format(x,y)
