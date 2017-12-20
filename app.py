from flask import Flask, request, jsonify
from config import HTTPMethodOverride
import controllers


app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)
version = "api/v1"

controllers = {
    'users': controllers.UsersController
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
def route(**params):

    try:
        controller = controllers[params['path']](
            params.get('id'),
            request.get_json(silent=True)
        )
    except Exception as e:
        return ("Bad Path", 404)

    method = getattr(controller, request.method.lower())
    return jsonify(method())


if __name__ == '__main__':
    app.run(debug=True)
