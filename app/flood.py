from pathlib import Path
from subprocess import Popen
from io import BytesIO

from PIL import Image, ImageDraw, ImageFilter

port_seedpoint_map = (
    ('felixstowe', (1000, 700)),
    ('hull', (1950, 600)),
    ('poole', (1950, 300)),
    ('portsmouth', (1250, 1250)),
    ('southampton', (900, 850)),
    ('panama', (2000, 500)),
    ('rotherdam', (2000, 1200)),
)


def parse_blob(blob):
    """
    Open blob as an Image instance.
    """
    return Image.open(BytesIO(blob))


def fill_image(orig_blob, seed_point, colors=2):
    """
    Process image: quantitize and fill, compute histogram,
    redo if the image has been filled poorly, e.g. has too much red.
    Don't go past 9 colour levels for quantitization.
    """
    img = parse_blob(orig_blob)
    img = quantize_and_fill(img, seed_point, colors)
    num_px = get_num_pixels(img)
    r_histo = get_r_histo(img)

    if (r_histo[-1] / num_px > 0.9) and colors < 9:
        print(f'Redoing with {colors+1} colors quantization...')
        img = fill_image(orig_blob, seed_point, colors=colors + 1)

    return img


def quantize_and_fill(img, seed_point, colors=2):
    """
    Load and transform.
    """
    img = (
        img.quantize(colors=colors, dither=Image.NEAREST, method=Image.MEDIANCUT)
        .convert('L')
        .convert('RGB')
    )
    ImageDraw.floodfill(img, xy=seed_point, value=(255, 0, 0))

    return img


def apply_additional_filters(img):
    return img.quantize(colors=2, dither=Image.NEAREST, method=Image.MEDIANCUT).convert(
        'RGB'
    )


def get_num_pixels(img):
    num_pixels = img.width * img.height
    return num_pixels


def get_r_histo(img):
    r, g, b = img.split()
    r_histo = r.histogram()
    return r_histo


def save_img(img, name):
    output = (
        f'output/{name}.bmp',
        f'output/{name}.png',
    )
    print(f'Saving {output}')

    for fn in output:
        img.save(fn)

    return output


def parse_one(blob, seedpoint, name):
    """
    Parse and save a single image.
    """
    print(f'Processing image: {name}')
    img = fill_image(blob, seedpoint)
    img = apply_additional_filters(img)
    return save_img(img, name)


def parse_file(name, seedpoint):
    blob = Path(f'images/{name}.png').read_bytes()
    return parse_one(blob, seedpoint, name)


def parse_all(port_seedpoint_map):
    return [parse_file(*port) for port in port_seedpoint_map]


def parse_geojson(filename):
    Popen(('potrace', filename, '-b', 'geojson'))


if __name__ == '__main__':
    parse_all(port_seedpoint_map)
    # parse_geojson(filenames)

    # Do a single image.
    # img = fill_image(*port_seedpoint_map[0])
    # img = apply_additional_filters(img)
    # save_img(img, 'test')
    # img.show()
