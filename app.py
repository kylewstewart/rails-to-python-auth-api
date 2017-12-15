from flask import Flask, request, jsonify
from http_method_override import HTTPMethodOverride
from controllers import user_contoller, auth_contoller

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)


@app.route("/api/v1/user", methods=['GET', 'POST'])
@app.route("/api/v1/user/<int:id>", methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def user_routes(**args):
    user = user_contoller.User(
        request.method,
        request.get_json(silent=True),
        args.get('id')
    )

    if args.get('id') is None:
        if request.method == 'GET':
            response = jsonify(user.index())
        elif request.method == 'POST':
            response = jsonify(user.create())
        else:
            response = ('', '500')
    else:
        if request.method == 'GET':
            response = jsonify(user.show())
        elif request.method == 'DELETE':
            response = jsonify(user.destroy())
        elif request.method == 'PUT' or request.method == 'PATCH':
            response = jsonify(user.update())
        else:
            response = ('', '500')

    return response


@app.route("/api/v1/auth", methods=['GET', 'POST'])
@app.route("/api/v1/auth/<int:id>", methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def auth_routes(**args):
    auth = auth_contoller.Auth(
        request.method,
        request.get_json(silent=True),
        args.get('id')
    )

    if args.get('id') is None:
        if request.method == 'GET':
            response = jsonify(auth.index())
        elif request.method == 'POST':
            response = jsonify(auth.create())
        else:
            response = ('', '500')
    else:
        if request.method == 'GET':
            response = jsonify(auth.show())
        elif request.method == 'DELETE':
            response = jsonify(auth.destroy())
        elif request.method == 'PUT' or request.method == 'PATCH':
            response = jsonify(auth.update())
        else:
            response = ('', '500')

    return response


if __name__ == '__main__':
    app.run(debug=True)
