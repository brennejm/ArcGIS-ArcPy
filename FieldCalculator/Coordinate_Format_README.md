# Coordinate_Format.py

## Description

Given two variables (longitude, latitude), it will round the coordinates and set the number of decimal places equal to numDec. It will also check to see if any of the ending digits rounded to zero and will pad the coordinates until they equal numDec.

## Assumptions

This script was written to expedite coordinate creation for large point datasets where a specific number of decimals is wanted or required. Prior to running this script, you should have two fields in your attribute table: one for longitude and one for latitude. These two fields can be string, float, or double. The script outputs coordinates as strings.

## Setup

Open the field calculator, select **Python** at the top, and select **Show Codeblock**. Copy and paste the script into the **Pre-Logic Script Code** area. In the field area, enter the following:

```
coordinates(numDec,!Lon!,!Lat!)
```

Make sure you change **numDec** to the number of decimal places required, and change **!Lon!** and **!Lat!** to the names for the fields in your table.

## Examples

**1 |** Rounding occurs without any ending zeros.

```
>>> print(coordinates(4,'-62.32893','20.87993'))
>>> -62.3289, 20.8799
```

**2 |** Rounding occurs with ending zeros.

```
>>> print(coordinates(4,'-62.32898','20.87998'))
>>> -62.3290, 20.8800
```

**3 |** Three decimal places are needed instead of four.

```
>>> print(coordinates(3,'-62.32898','20.87998'))
>>> -62.329, 20.880
```

**4 |** Using variables.

```
>>> numDec = 3
>>> longitude = '-62.32898'
>>> latitude = '20.87998'
>>> print(coordinates(numDec,longitude,latitude))
>>> -62.329, 20.880
```
