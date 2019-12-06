from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# Load
img = Image.open('images/southampton_colour.png')

# Transform
img = img.quantize(colors=4, dither=Image.NEAREST, method=Image.MEDIANCUT).convert('RGB')
# img = img.filter(filter=ImageFilter.EDGE_ENHANCE_MORE)

# Port coordinate
seed_point = (900, 850)

out = ImageDraw.floodfill(img, xy=seed_point, value=(122,0,0,255))

print('Image size: ', img.getbbox())

img.show()
