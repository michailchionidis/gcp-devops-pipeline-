from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import main

app = Flask(__name__)

# Load environment variables
load_dotenv()

@app.route('/', methods=['POST'])
def extract():
    response = main.main(request)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))