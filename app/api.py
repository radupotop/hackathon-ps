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


# def save_blob(data: bytes):
#     """
#     Save image blob.
#     """
#     ts = datetime.utcnow().isoformat()
#     fp = f'images/{ts}'
#     Path(fp).write_bytes(data)
#     return ts


def parse_seedpoint(seed):
    return tuple(map(int, seed.split(',')))


@Request.application
def application(request):

    seedpoint, data = request.args.get('seedpoint'), request.get_data()
    sp = parse_seedpoint(seedpoint)

    if not (sp and validate_blob(data)):
        return Response('"Params are rubbish"', status=400, content_type='application/problem+json')

    # Save image blob
    # ts = save_blob(data)
    ts = datetime.utcnow().isoformat()
    parse_one(data, sp, ts)
    f = Path(f'output/{ts}.png').read_bytes()

    return Response(f, mimetype='image/png', content_type='image/png')
    # return response(environ, start_response)

    # return Response("Hello, World!")

if __name__ == "__main__":
    run_simple("localhost", 5000, application)
