"""
1. Find a seed point (the original port coordinates).
2. Do an quantitize and fill on the map to detect edges.
    - This detects points of interest such as terminals and berths.
3. Put bounding boxes around those POIs and built Rtrees in PostGIS
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# Load
img = Image.open('images/southampton_colour.png')

# Transform
img = img.quantize(colors=4, dither=Image.NEAREST, method=Image.MEDIANCUT).convert('RGB')

# Port coordinate
seed_point = (900, 850)

# img = img.filter(filter=ImageFilter.FIND_EDGES)
ImageDraw.floodfill(img, xy=seed_point, value=(127,0,0,0))

print('Image size: ', img.getbbox())

img.show()
