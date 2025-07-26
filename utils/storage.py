# database simuation:
# saves submissions to a JSON file

import json
import os

def save_post(name, message, tag):
    file_path = 'data/posts.json'
    os.makedirs('data', exist_ok=True)

    posts = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
                if content:
                    posts = json.loads(content)
        except (json.JSONDecodeError, ValueError):
            posts = []

    posts.append({
        'name': name,
        'message': message,
        'tag': tag,
        'likes': 0
    })

    with open(file_path, 'w') as f:
        json.dump(posts, f, indent=2)

def update_likes(index):
    file_path = 'data/posts.json'
    with open(file_path, 'r') as f:
        posts = json.load(f)

    if 0 <= index < len(posts):
        posts[index]['likes'] += 1

    with open(file_path, 'w') as f:
        json.dump(posts, f, indent=2)