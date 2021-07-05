from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello')
def hello():
    json_file = {}
    json_file['query'] = 'hellow'
    return jsonify(json_file)

@app.route('/world')
def world():
    json_file = {}
    json_file['query'] = 'worldy'
    return jsonify(json_file)


if __name__ == '__main__':
    app.run()
