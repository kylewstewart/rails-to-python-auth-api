from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from libraries import HTTPMethodOverride, authorize, cors
import controllers
from IPython import embed

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)
version = "api/v1"

controllers = {
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
@authorize
def route(**params):

    if request.method == 'OPTIONS':
        data = ""
        code = 200
    else:
        if request.authorized is False:
            controller = controllers['auth']()
            method = getattr(controller, 'create')
            data, code = method()
        else:
            try:
                controller = controllers[params['path']]()
                method = getattr(controller, request.method.lower())
                data, code = method()
            except Exception as e:
                data = {'error': "Bad Path"}
                code = 404

    resp = make_response(jsonify(data), code)
    resp = cors(resp)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
