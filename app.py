
from flask import Flask, request, jsonify
from http_method_override import HTTPMethodOverride


app = Flask(__name__)
app.wsgi_app = HTTPMethodOverride(app.wsgi_app)


@app.route('/api/v1/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        data = dict()
        data['msg'] = "User#Index"
        return jsonify(data)
    elif request.method == 'POST':
        req_data = request.get_json()
        return jsonify(req_data)


if __name__ == '__main__':
    app.run(debug=True)
