# Text Embeddings API

This project provides a REST API for generating text embeddings using the Sentence Transformers model. It is built using Flask and aims to simplify the process of converting text into embeddings for various NLP tasks.

## Features

- **Text Embedding Generation**: Converts input text into embeddings using the `BAAI/bge-base-zh` model.
- **Error Handling**: Robust error handling to manage missing fields and unexpected errors.
- **Logging**: Comprehensive logging for monitoring API requests and debugging.

## Usage

### API Endpoint

- **POST `/`**: Accepts a JSON payload with a `text` field and returns the corresponding embeddings.

### Example Request

```bash
curl -X POST http://<server_address>/ -H "Content-Type: application/json" -d '{"text": "Your text here"}'
```

### Example Response

```json
{
  "Embeddings": [...]
}
```

## Complexity and Challenges

### 1. Model Integration
- **Complexity**: Integrating the Sentence Transformers model and ensuring it loads correctly.
- **Solution**: Used `SentenceTransformer` from the `sentence_transformers` package to load the pre-trained model.

### 2. Error Handling
- **Complexity**: Handling errors gracefully, such as missing fields or model failures.
- **Solution**: Implemented try-except blocks to catch and log errors, returning appropriate HTTP status codes.

### 3. Logging
- **Complexity**: Ensuring comprehensive logging for debugging and monitoring.
- **Solution**: Configured logging to capture all levels of logs and included detailed log messages.

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- sentence-transformers

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/faisal-fida/text-embeddings-API.git
   cd text-embeddings-API
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python main.py
   ```

## Conclusion

This API provides an efficient and straightforward approach to generating text embeddings, with robust error handling and logging to ensure reliability. It is ideal for applications needing quick and accurate text representation for NLP tasks.
