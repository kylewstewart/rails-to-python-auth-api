from flask import Flask, request, make_response, jsonify
from libraries import HTTPMethodOverride, is_authorized, cors
from config import authorize
import controllers

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)
version = "api/v1"

routes = {
    'user': controllers.UsersController,
    'auth': controllers.AuthController,
}


@app.route(
    f"/{version}/<path>",
    defaults={'id': None},
    methods=['GET', 'POST', 'OPTIONS']
)
@app.route(
    f"/{version}/<path>/<int:id>",
    methods=['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
)
def route(**params):
    path = params['path']
    method = request.method

    if method == 'OPTIONS':
        data, code = ('', 200)
    elif method in authorize[path]:
        if is_authorized():
            data, code = getattr(routes[path](), method.lower())()
        else:
            data, code = ({'error': 'Authoization Failed'}, 401)
    else:
        try:
            data, code = getattr(routes[path](), method.lower())()
        except Exception as e:
            data, code = ({'error': "Bad Path"}, 404)

    resp = make_response(jsonify(data), code)
    resp = cors(resp)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
