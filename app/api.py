from datetime import datetime
from pathlib import Path
from io import BytesIO

import magic
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

from flood import parse_geojson, parse_one


def validate_blob(data: bytes):
    datum = magic.from_buffer(data)
    return str(datum).startswith('PNG image')


def parse_seedpoint(seed):
    if seed:
        return tuple(map(int, seed.split(',')))


@Request.application
def application(request):

    seedpoint, data = request.args.get('seedpoint'), request.get_data()
    sp = parse_seedpoint(seedpoint)

    if not (sp and validate_blob(data)):
        return Response('"Params are rubbish"', status=400, content_type='application/problem+json')

    # Save image blob
    ts = datetime.utcnow().isoformat()
    parse_one(data, sp, ts)
    parsed_file = Path(f'output/{ts}.png').read_bytes()

    if not parsed_file:
        return Response('"No output file found"', status=400, content_type='application/problem+json')

    return Response(parsed_file, mimetype='image/png', content_type='image/png')


if __name__ == "__main__":
    run_simple("0.0.0.0", 5000, application)
