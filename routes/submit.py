from flask import Blueprint, request, jsonify
from utils.storage import save_post, update_likes
import json

forum_bp = Blueprint('forum', __name__)

@forum_bp.route('/submit', methods=['POST'])
def submit_post():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')
    tag = data.get('tag')

    if not name or not message:
        return jsonify({'error': 'All fields are required'}), 400

    try:
        save_post(name, message, tag)
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
        posts.reverse()
        return jsonify(posts)
    except Exception as e:
        return jsonify({'error': f'Could not load posts: {str(e)}'}), 500

@forum_bp.route('/like/<int:index>', methods=['POST'])
def like_post(index):
    try:
        update_likes(index)
        return jsonify({'message': 'Liked!'})
    except Exception as e:
        return jsonify({'error': f'Could not update likes: {str(e)}'}), 500