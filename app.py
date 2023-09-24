from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main_page():
    text_string = request.get_json()
    return jsonify(text_string)