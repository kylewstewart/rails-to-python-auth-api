from flask import request
from IPython import embed


def cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = request.environ.get(
        'HTTP_ORIGIN', '*'
    )
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    resp.headers['Access-Control-Allow-Headers'] = request.headers.get(
        'Access-Control-Request-Headers', 'Authorization')
    return resp
