# database simuation:
# saves submissions to a JSON file

import json
import os # we need this to check if certain files exist

DATA_FILE = 'data/submissions.json' # save the name of the data file for easy use

def save_post(name, message):
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

    posts.append({'name': name, 'message': message})

    with open(file_path, 'w') as f:
        json.dump(posts, f, indent=2)
