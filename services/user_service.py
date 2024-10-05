from db import get_db_connection
import logging
import bcrypt
from utils.jwt_auth import encode_jwt
import sys
import traceback

# Setup logging to output to both console and file
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for detailed logs
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Log to console
        logging.FileHandler("app.log")      # Log to a file
    ]
)
logger = logging.getLogger(__name__)

class UserService:
    @staticmethod
    def register_user(username, email, password):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Insert the new user into the database
            query = "INSERT INTO user (username, email, password_hash) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, hashed_password))
            conn.commit()
            conn.close()
            return {'message': 'User registered successfully'}, 201
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            return {'message': 'Error registering user'}, 500

    @staticmethod
    def login_user(email, password):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Retrieve the user by email
            query = "SELECT id, password_hash FROM user WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            conn.close()

            if not user:
                return {'message': 'User not found'}, 404

            user_id, stored_password = user

            # Check if the provided password matches the stored hash
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # Generate a JWT token for the authenticated user
                token = encode_jwt(user_id)
                return {'message': 'Login successful', 'token': token}, 200
            else:
                return {'message': 'Incorrect password'}, 401
        except Exception as e:
            logger.error(f"Error logging in user: {e}")
            return {'message': 'Error logging in'}, 500
