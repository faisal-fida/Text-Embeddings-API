from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main_page():
    try:
        text_string = request.get_json()
        return jsonify(text_string)

    except Exception as e:
        response_error = {'Error':e}
        return response_error, 500

app.run()