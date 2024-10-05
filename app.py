from flask import Flask
from controllers.post_controller import post_controller
from controllers.user_controller import user_controller
from controllers.comment_controller import comment_controller
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS to allow requests from frontend applications
CORS(app)

# Setup rate limiting to prevent abuse (200 requests per day, 50 per hour)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Register blueprints (route handlers) for posts, users and comments
app.register_blueprint(post_controller)
app.register_blueprint(user_controller)
app.register_blueprint(comment_controller)

# Setup logging for error tracking
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

# Handle uncaught exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Error: {str(e)}")
    return {'message': 'An error occurred'}, 500

# Run the Flask app
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=5000)
