from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

port_seedpoint_map = (
    ('felixstowe', (1000, 700)),
    ('hull', (1950, 600)),
    ('poole', (1950, 300)),
    ('portsmouth', (1250, 1250)),
    ('southampton', (900, 850)),
    ('panama', (2000, 500)),
)


def fill_image(name, seed_point):
    # Load
    img = Image.open(f'images/{name}.png')

    # Transform
    img = img.quantize(colors=3, dither=Image.NEAREST, method=Image.MEDIANCUT).convert('L').convert('RGB')

    # img = img.filter(filter=ImageFilter.FIND_EDGES)
    ImageDraw.floodfill(img, xy=seed_point, value=(127,0,0,0))

    print('Image size: ', img.getbbox())

    img.save(f'output/{name}.png')


for port in port_seedpoint_map:
    fill_image(*port)
