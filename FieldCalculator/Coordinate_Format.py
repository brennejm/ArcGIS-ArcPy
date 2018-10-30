## Program: Coordinate Format
## Description: Given two variables (longitude, latitude), it
## will round the coordinates, set the number of decimal
## places equal to numDec, and return a string.

def coordinates(lon,lat):
    # Set numDec equal to how many decimal places you want.
    numDec = 4

    x = str(round(float(lon),numDec))
    y = str(round(float(lat),numDec))

    # If any ending digits rounded to zero, pad the coordinate to equal numDec.
    if len(x[x.find('.')+1:]) < numDec:
        while len(x[x.find('.')+1:]) < numDec:
            x = x + '0'

    if len(y[y.find('.')+1:]) < numDec:
        while len(y[y.find('.')+1:]) < numDec:
            y = y + '0'
            
    return '{}, {}'.format(x,y)
