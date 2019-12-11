from werkzeug.wrappers import Request, Response

from flood import parse_one, parse_geojson


@Request.application
def application(request):
    if not (request.args.get('place') and request.args.get('seed') and request.data):
        return Response('"Params are rubbish, mate"', status=400, content_type='application/json')

    # code goes here.

    return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)
