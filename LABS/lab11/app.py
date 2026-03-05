# app.py
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# --- In-Memory Data Store (for simplicity) ---
# In a real application, this would be a database.
tasks = [
    {
        'id': 1,
        'title': 'Learn Python',
        'description': 'Complete a Python course to understand the basics.',
        'done': True
    },
    {
        'id': 2,
        'title': 'Build a REST API',
        'description': 'Use Flask to create a simple RESTful API.',
        'done': False
    }
]

# --- API Endpoints ---

# [READ] GET /tasks
# Retrieve the list of all tasks.
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# [READ] GET /tasks/<int:task_id>
# Retrieve a single task by its ID.
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Find the task with the matching ID
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        # If no task is found, return a 404 Not Found error
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

# [CREATE] POST /tasks
# Create a new task.
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        # Return a 400 Bad Request if the request is not JSON or is missing a title
        return jsonify({'error': 'Bad Request: Missing title in request body'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1, # Simple ID generation
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(new_task)
    # Return the new task with a 201 Created status code
    return jsonify({'task': new_task}), 201

# [UPDATE] PUT /tasks/<int:task_id>
# Update an existing task.
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad Request: Invalid JSON'}), 400

    # Update fields if they are provided in the request body
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

# [DELETE] DELETE /tasks/<int:task_id>
# Delete a task.
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks.remove(task)
    return jsonify({'result': True})

# This allows the script to be run directly.
if __name__ == '__main__':
    # The host='0.0.0.0' makes the server accessible from your network.
    # debug=True will auto-reload the server when you make changes.
    app.run(host='0.0.0.0', port=5000, debug=True)
