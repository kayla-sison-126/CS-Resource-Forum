from flask import Flask, jsonify, render_template
from routes.submit import forum_bp
import os
import json
import logging
logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
app.register_blueprint(forum_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates/writePost.html')
def writePost():
    return render_template('writePost.html')

@app.route('/templates/index.html')
def index():
    return render_template('index.html')

@app.route('/submissions', methods=['GET'])
def get_submissions():
    file_path = 'data/submissions.json'
    
    if not os.path.exists(file_path):
        return jsonify([]), 200

    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return jsonify({"error": "Data is corrupted"}), 500

    return jsonify(data), 200

@app.route('/health', methods=['GET']) # for testing purposes
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
