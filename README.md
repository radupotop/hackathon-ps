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


## Potrace

    potrace felixstowe.bmp -b geojson


From the SeedPoint determine the origin of the map (x0, y0 coordinates).


## Example CLI calls

    http --timeout 120 http://localhost:5000/ seedpoint==0,0 @images/southampton.png -d -o output/southampton.png

    http --timeout 120 http://localhost:5000/ seedpoint==1000,700 @images/felixstowe.png -d -o output/felixstowe.png
