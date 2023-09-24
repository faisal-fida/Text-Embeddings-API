import logging
from flask import Flask
from flask import jsonify, request
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__)

app = Flask(__name__)
model = SentenceTransformer('BAAI/bge-base-zh')

def make_embeddings(text_string):
    sentences = [text_string]

    try:
        embeddings = model.encode(sentences)
        return embeddings
    
    except Exception as e:
        error_msg = {'Error': e}
        logging.error(f'Got Error: {error_msg["Error"]}')
        return error_msg, 403

@app.route('/', methods=['POST'])
def embed_text():

    try:
        text_string = request.get_json()
        logging.info('Got JSON_DATA.')

        if 'text' not in text_string:
            error_msg = {'Error':'Missing text field in JSON_DATA.'}
            logging.error(error_msg['Error'])
            return error_msg, 400
        
        embeddings = make_embeddings(text_string['text'])
        logging.info('Embeddings:')
        logging.info(f'{embeddings}')
        final_embeddings = {'Embeddings':embeddings}
        return final_embeddings, 200
    
    except Exception as e:
        error_msg = {'Error':e}
        logging.error(f'Got Error: {error_msg["Error"]}')
        return error_msg, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')