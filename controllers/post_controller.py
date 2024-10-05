from flask import Blueprint, request, jsonify
from services.post_service import PostService
from utils.jwt_auth import jwt_required

# Blueprint for managing post-related routes
post_controller = Blueprint('post_controller', __name__)

# Route to create a new post
@post_controller.route('/post', methods=['POST'])
@jwt_required
def create_post(user_id):
    data = request.get_json()
    return PostService.create_post(user_id, data['content'])

# Route to update an existing post
@post_controller.route('/post/<int:post_id>', methods=['PUT'])
@jwt_required
def update_post(user_id, post_id):
    data = request.get_json()
    return PostService.update_post(post_id, data['content'])

# Route to delete a post
@post_controller.route('/post/<int:post_id>', methods=['DELETE'])
@jwt_required
def delete_post(user_id, post_id):
    return PostService.delete_post(post_id)

# Route to get a post by its ID
@post_controller.route('/post/<int:post_id>', methods=['GET'])
@jwt_required
def get_post(user_id, post_id):
    return jsonify(PostService.get_post(post_id))
