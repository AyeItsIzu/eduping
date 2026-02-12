from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='public', static_url_path='')
msgs = []

@app.route('/api/msg', methods=['POST'])
def save():
    msgs.append(request.json['text'])
    return jsonify(ok=True)

@app.route('/api/msg', methods=['GET'])
def load():
    return jsonify(msgs[-20:])

@app.route('/')
def home():
    return app.send_static_file('index.html')
