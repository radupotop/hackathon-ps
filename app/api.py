from datetime import datetime
from pathlib import Path

from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

from flood import parse_geojson, parse_one


def save_blob(data: bytes):
    """
    Save image blob.
    """
    ts = datetime.utcnow().isoformat()
    fp = f'images/{ts}'
    Path(fp).write_bytes(data)
    return ts


def parse_seedpoint(seed):
    return tuple(map(int, seed.split(',')))


@Request.application
def application(request):

    seedpoint, data = request.args.get('seedpoint'), request.get_data()

    if not (seedpoint and data):
        return Response('"Params are rubbish"', status=400, content_type='application/problem+json')

    # Save image blob
    ts = save_blob(data)

    # code goes here.
    parsed = parse_one((ts, parse_seedpoint(seedpoint)))

    return Response("Hello, World!")

if __name__ == "__main__":
    run_simple("localhost", 5000, application)
