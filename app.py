from flask import Flask, request
from flask_cors import CORS
from libraries import HTTPMethodOverride, authorize
import controllers

app = Flask(__name__)
CORS(app)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)
version = "api/v1"

controllers = {
    'user': controllers.UsersController,
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
    return method()


if __name__ == '__main__':
    app.run(debug=True)
