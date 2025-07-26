from flask import Blueprint, request, jsonify
from utils.storage import save_post
import json

forum_bp = Blueprint('forum', __name__)

@forum_bp.route('/submit', methods=['POST'])
def submit_post():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({'error': 'Name and message are required'}), 400

    try:
        save_post(name, message)
        return jsonify({'message': 'Post submitted successfully!'})
    except Exception as e:
        return jsonify({'error': f'Failed to save post: {str(e)}'}), 500

@forum_bp.route('/posts', methods=['GET'])
def get_posts():
    try:
        with open('data/posts.json', 'r') as f:
            content = f.read().strip()
            if content:
                posts = json.loads(content)
            else:
                posts = []
        return jsonify(posts)
    except Exception as e:
        return jsonify({'error': f'Could not load posts: {str(e)}'}), 500
