# app/routes/auth_routes.py
from flask import Blueprint, request, jsonify
from app.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = generate_password_hash(data['password'])

        if User.query.filter_by(email=email).first():
            return jsonify({"message": "Email already registered"}), 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong"}), 500
   
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user=User.query.filter_by(username=data['username']).first()

    if user and user.check_password(password):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token),200
    return jsonify({"message": "Invalid credentials"}),401