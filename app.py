from flask import Flask, request, jsonify
from libraries import HTTPMethodOverride, authorize
import controllers
from IPython import embed

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)
version = "api/v1"

controllers = {
    'users': controllers.UsersController,
    'auth': controllers.AuthController
}


@app.route(
    f"/{version}/<path>",
    defaults={'id': None},
    methods=['GET', 'POST']
)
@app.route(
    f"/{version}/<path>/<int:id>",
    methods=['GET', 'PUT', 'PATCH', 'DELETE']
)
@authorize
def route(**params):
    if request.authorized is True:
        try:
            controller = controllers[params['path']]()
        except Exception as e:
            return ("Bad Path", 404)
        method = getattr(controller, request.method.lower())
    else:
        controller = controllers['auth']()
        method = getattr(controller, 'create')
    return jsonify(method())


if __name__ == '__main__':
    app.run(debug=True)
