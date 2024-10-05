import jwt
from flask import request, jsonify
from functools import wraps
from config import Config
import datetime

# Encode JWT token with user ID
def encode_jwt(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=Config.JWT_EXPIRATION),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

# Decode JWT token and retrieve user ID
def decode_jwt(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

# Decorator to protect routes that require authentication
def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            token = token.split(" ")[1]  # Extract the token from "Bearer <token>"
        except IndexError:
            return jsonify({'message': 'Token format invalid!'}), 403
        
        user_id = decode_jwt(token)
        if not isinstance(user_id, int):
            return jsonify({'message': user_id}), 403  # Return error message
        return f(user_id, *args, **kwargs)
    return decorated_function
