from flask import Flask, jsonify
import gdown

app = Flask(__name__)


# Route to indicate that the server is running
@app.route('/')
def server_running():
    return jsonify(message='Server is running')

@app.route('/run-colab')
def run_colab():
    file_id = "1iGLQAtupTFPTPhtdWVg3Q5ECR7gR1cYY"
    gdown.download(f'https://drive.google.com/uc?id={file_id}', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')

# Ignore favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 404
