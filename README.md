## Flood fill

1. Find a seed point (the original port coordinates).
    - Will be semi-automated.
2. Do a quantitize and fill on the map to detect land edges.
    - This detects the outline of Points Of Interest such as terminals and berths.
3. Put bounding boxes around those POIs and built Rtrees indices in PostGIS
    - Determine bounding boxes
    - Create PostGIS polygons from them


## Quantitize process

- Process image: quantitize and fill, compute histogram,
  redo if the image has been filled poorly, e.g. has too much red.
- Don't go past 9 colour levels for quantitization.
- Apply additional filters if necessary.
