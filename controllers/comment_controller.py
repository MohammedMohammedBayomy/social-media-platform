from flask import Blueprint, request, jsonify
from services.comment_service import CommentService
from utils.jwt_auth import jwt_required

# Blueprint for managing comment-related routes
comment_controller = Blueprint('comment_controller', __name__)

# Route to add a comment to a post
@comment_controller.route('/post/<int:post_id>/comment', methods=['POST'])
@jwt_required
def add_comment(user_id, post_id):
    data = request.get_json()
    return CommentService.add_comment(user_id, post_id, data['content'])

# Route to delete a comment
@comment_controller.route('/comment/<int:comment_id>', methods=['DELETE'])
@jwt_required
def delete_comment(user_id, comment_id):
    return CommentService.delete_comment(comment_id)

# Route to get all comments for a post
@comment_controller.route('/post/<int:post_id>/comments', methods=['GET'])
@jwt_required
def get_comments(post_id):
    return jsonify(CommentService.get_comments_for_post(post_id))