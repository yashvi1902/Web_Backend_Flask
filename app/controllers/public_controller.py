# app/controllers/public_controller.py

from flask import Blueprint, jsonify

public_bp = Blueprint('public_bp', __name__)

# Sample list of public items (could be fetched from a database)
public_items = [
    {"id": 1, "name": "Item 1", "description": "This is a public item."},
    {"id": 2, "name": "Item 2", "description": "This is another public item."},
    {"id": 3, "name": "Item 3", "description": "This is yet another public item."}
]

# Public route for retrieving public information
@public_bp.route('/public', methods=['GET'])
def public_info():
    return jsonify(public_items), 200
