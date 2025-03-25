# app/controllers/db_controller.py
from flask import Blueprint, request, jsonify
from .. import mysql

db_bp = Blueprint('db_bp', __name__)

# CREATE User
@db_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    if not username or not password or not email:
        return jsonify(message="All fields (username, password, email) are required."), 400
    
    # Create new user in the database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
    mysql.connection.commit()
    cur.close()
    
    return jsonify(message="User created successfully."), 201

# READ All Users
@db_bp.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username, email FROM users")  # Only fetching essential fields
    result = cur.fetchall()
    cur.close()
    
    users = []
    for user in result:
        users.append({
            'id': user[0],
            'username': user[1],
            'email': user[2]
        })
    
    return jsonify(users), 200

# READ Single User by ID
@db_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username, email FROM users WHERE id = %s", (user_id,))
    result = cur.fetchone()
    cur.close()
    
    if result:
        user = {
            'id': result[0],
            'username': result[1],
            'email': result[2]
        }
        return jsonify(user), 200
    return jsonify(message="User not found."), 404

# UPDATE User by ID
@db_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    if not username or not password or not email:
        return jsonify(message="All fields (username, password, email) are required."), 400
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET username = %s, password = %s, email = %s WHERE id = %s", (username, password, email, user_id))
    mysql.connection.commit()
    cur.close()
    
    return jsonify(message="User updated successfully."), 200

# DELETE User by ID
@db_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify(message="User deleted successfully."), 200
