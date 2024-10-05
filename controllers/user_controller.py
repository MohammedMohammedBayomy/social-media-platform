from flask import Blueprint, request, jsonify
from services.user_service import UserService

# Blueprint for handling user-related routes
user_controller = Blueprint('user_controller', __name__)

# Route to register a new user
@user_controller.route('/register', methods=['POST'])
def register_user():
    print('register_user')
    data = request.get_json()
    return UserService.register_user(data['username'], data['email'], data['password'])

# Route for user login
@user_controller.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    return UserService.login_user(data['email'], data['password'])
