from flask import Flask, request, jsonify
from http_method_override import HTTPMethodOverride
from controllers import user_contoller
from IPython import embed

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)


@app.route("/api/v1/user", methods=['GET', 'POST'])
@app.route("/api/v1/user/<int:id>", methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def user_routes(**args):
    method = request.method
    data = request.get_json(silent=True)
    id = args.get('id')
    user = user_contoller.User(method, data, id)

    if id is None:
        if method == 'GET':
            response = jsonify(user.index())
        elif method == 'POST':
            response = jsonify(user.create())
        else:
            response = ('', '500')
    else:
        if method == 'GET':
            response = jsonify(user.show())
        elif method == 'DELETE':
            response = jsonify(user.destroy())
        elif method == 'PUT' or method == 'PATCH':
            response = jsonify(user.update())
        else:
            response = ('', '500')

    return response


if __name__ == '__main__':
    app.run(debug=True)
