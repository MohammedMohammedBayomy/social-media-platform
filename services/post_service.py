import bleach
from db import get_db_connection
import logging

logger = logging.getLogger(__name__)

class PostService:
    @staticmethod
    def create_post(user_id, content):
        try:
            # Sanitize the content to prevent XSS
            safe_content = bleach.clean(content)

            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO post (user_id, content) VALUES (%s, %s)"
            cursor.execute(query, (user_id, safe_content))
            conn.commit()
            post_id = cursor.lastrowid
            conn.close()
            return {'message': 'Post created', 'post_id': post_id}, 201
        except Exception as e:
            logger.error(f"Error creating post: {e}")
            return {'message': 'Error creating post'}, 500

    @staticmethod
    def update_post(post_id, user_id, content):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if the post belongs to the user
            query = "SELECT user_id FROM post WHERE id = %s"
            cursor.execute(query, (post_id,))
            result = cursor.fetchone()

            if not result:
                return {'message': 'Post not found'}, 404

            post_owner_id = result[0]
            if post_owner_id != user_id:
                return {'message': 'Unauthorized: You do not own this post'}, 403

            # Sanitize the content to prevent XSS
            safe_content = bleach.clean(content)

            query = "UPDATE Post SET content = %s WHERE id = %s"
            cursor.execute(query, (safe_content, post_id))
            conn.commit()
            conn.close()
            return {'message': 'Post updated successfully'}, 200
        except Exception as e:
            logger.error(f"Error updating post: {e}")
            return {'message': 'Error updating post'}, 500

    @staticmethod
    def delete_post(post_id, user_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if the post belongs to the user
            query = "SELECT user_id FROM post WHERE id = %s"
            cursor.execute(query, (post_id,))
            result = cursor.fetchone()

            if not result:
                return {'message': 'Post not found'}, 404

            post_owner_id = result[0]
            if post_owner_id != user_id:
                return {'message': 'Unauthorized: You do not own this post'}, 403

            query = "DELETE FROM Post WHERE id = %s"
            cursor.execute(query, (post_id,))
            conn.commit()
            conn.close()
            return {'message': 'Post deleted successfully'}, 200
        except Exception as e:
            logger.error(f"Error deleting post: {e}")
            return {'message': 'Error deleting post'}, 500

    @staticmethod
    def get_post(post_id, user_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM post WHERE id = %s"
            cursor.execute(query, (post_id,))
            post = cursor.fetchone()
            conn.close()

            if not post:
                return {'message': 'Post not found'}, 404

            post_owner_id = post[1]
            is_owner = post_owner_id == user_id

            post_data = {
                'post_id': post[0],
                'user_id': post_owner_id,
                'content': bleach.clean(post[2]),  # Sanitize output as well (extra safety)
                'is_owner': is_owner
            }

            return post_data, 200
        except Exception as e:
            logger.error(f"Error retrieving post: {e}")
            return {'message': 'Error retrieving post'}, 500
