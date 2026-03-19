# blog_api.py
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory data store for blog posts
posts = [
    {
        'id': 1,
        'title': 'Introduction to REST APIs',
        'content': 'This post explains what REST APIs are and why they are important.',
        'author': 'Alice',
        'date_posted': '2025-08-09T19:30:00Z'
    },
    {
        'id': 2,
        'title': 'Getting Started with Flask',
        'content': 'A beginner-friendly guide to setting up a Flask application.',
        'author': 'Bob',
        'date_posted': '2025-08-09T20:15:00Z'
    }
]
next_post_id = 3

# [READ] Get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})

# [READ] Get a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'post': post})

# [CREATE] Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not all(k in request.json for k in ['title', 'content', 'author']):
        return jsonify({'error': 'Bad Request: Missing title, content, or author'}), 400
    
    global next_post_id
    new_post = {
        'id': next_post_id,
        'title': request.json['title'],
        'content': request.json['content'],
        'author': request.json['author'],
        'date_posted': datetime.utcnow().isoformat() + 'Z' # Use ISO 8601 format
    }
    posts.append(new_post)
    next_post_id += 1
    return jsonify({'post': new_post}), 201

# [UPDATE] Update an existing post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad Request: Invalid JSON'}), 400

    post['title'] = request.json.get('title', post['title'])
    post['content'] = request.json.get('content', post['content'])
    return jsonify({'post': post})

# [DELETE] Delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    post_to_delete = next((p for p in posts if p['id'] == post_id), None)
    if post_to_delete is None:
        return jsonify({'error': 'Post not found'}), 404
    
    posts = [p for p in posts if p['id'] != post_id]
    return jsonify({'result': True, 'message': 'Post deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
