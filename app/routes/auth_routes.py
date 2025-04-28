# app/routes/auth_routes.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({"message": "User registered successfully", "data": data})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({"message": "User logged in successfully", "data": data})
