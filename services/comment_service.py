from db import get_db_connection
import logging

logger = logging.getLogger(__name__)

class CommentService:
    @staticmethod
    def add_comment(user_id, post_id, content):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO Comment (user_id, post_id, content) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, post_id, content))
            conn.commit()
            comment_id = cursor.lastrowid
            conn.close()
            return {'message': 'Comment added', 'comment_id': comment_id}, 201
        except Exception as e:
            logger.error(f"Error adding comment: {e}")
            return {'message': 'Error adding comment'}, 500

    @staticmethod
    def delete_comment(comment_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM Comment WHERE id = %s"
            cursor.execute(query, (comment_id,))
            conn.commit()
            conn.close()
            return {'message': 'Comment deleted'}, 200
        except Exception as e:
            logger.error(f"Error deleting comment: {e}")
            return {'message': 'Error deleting comment'}, 500

    @staticmethod
    def get_comments_for_post(post_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Comment WHERE post_id = %s"
            cursor.execute(query, (post_id,))
            comments = cursor.fetchall()
            conn.close()
            if comments:
                return comments, 200
            return {'message': 'No comments found'}, 404
        except Exception as e:
            logger.error(f"Error retrieving comments: {e}")
            return {'message': 'Error retrieving comments'}, 500
