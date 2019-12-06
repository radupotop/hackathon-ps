## Flood fill

1. Find a seed point (the original port coordinates).
    - Will be semi-automated.
2. Do a quantitize and fill on the map to detect land edges.
    - This detects points of interest such as terminals and berths.
3. Put bounding boxes around those POIs and built Rtrees indices in PostGIS
