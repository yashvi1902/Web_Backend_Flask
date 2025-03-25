
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from ..models.user import User

auth_bp = Blueprint('auth_bp', __name__)

# User login route
@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

 # Log the username and password received in the request
    print(f"Username: {username}")
    print(f"Password: {password}")
    # Authenticate the user by checking the username and password
    user = User.get_user_by_username(username)
    
    print(f"User: {user.password}")
    
    if not user or not User.check_password(password, user.password):
        return jsonify({"msg": "Invalid credentials"}), 401

    # Generate JWT token for the authenticated user
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# User registration route
@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Check if username already exists
    if User.get_user_by_username(username):
        return jsonify({"msg": "Username already exists"}), 400

    # Create new user
    User.create_user(username, password)
    return jsonify({"msg": "User created successfully"}), 201

# Protected route that requires authentication
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="This is a protected route"), 200
