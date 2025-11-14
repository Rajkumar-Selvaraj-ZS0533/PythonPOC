from flask import Blueprint, jsonify, request
from app.models.User import User
from app.services.user_service import get_user_by_id, get_all_user, save_user, edit_user_details, delete_user_details

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/all', methods=['GET'])
def get_user_all():
    users = get_all_user()
    if users:
        return jsonify([user.to_dict() for user in users]), 200
    return jsonify({'message': 'User not found'}), 404


@user_bp.route('/create', methods=['POST'])
def handle_post():
    
    data = request.get_json()

    
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    
    name = data.get('name')
    email = data.get('email')

    user = User()
    user.email = email
    user.name = name
    save_user(user)
    
    if not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    
    response = {
        "message": "Data received successfully",
        "name": name,
        "email": email
    }
    return jsonify(response), 200

@user_bp.route('/edit/<int:user_id>', methods = ['PUT'])
def edit_user(user_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    

    edit_user_details(user_id , data.get('name'), data.get('email'))

    return jsonify({
        "message": "User updated successfully",
        "id": user_id,
        "name": data.get('name'),
        "eamil": data.get('email')
    }), 200


@user_bp.route('/delete/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    

    delete_user_details(user_id)

    return jsonify({
        "message": "User deleted successfully",
    }), 200
