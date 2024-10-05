import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Database credentials
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DB = os.getenv('MYSQL_DB')

    # JWT Secret Key
    SECRET_KEY = os.getenv('SECRET_KEY')

    # JWT Token Expiration Time (in seconds)
    JWT_EXPIRATION = int(os.getenv('JWT_EXPIRATION', 3600))