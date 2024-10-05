import mysql.connector
from mysql.connector import pooling
from config import Config

# Database configuration for connection pooling
dbconfig = {
    "host": Config.MYSQL_HOST,
    "user": Config.MYSQL_USER,
    "password": Config.MYSQL_PASSWORD,
    "database": Config.MYSQL_DB
}

# Connection pool to optimize DB connections
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,  # Maximum 10 connections at a time
    **dbconfig
)

# Function to get a connection from the pool
def get_db_connection():
    return connection_pool.get_connection()
