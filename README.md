
# Social Media Platform API

## Project Overview

This is a basic social media platform API that allows users to create accounts, create posts, comment on posts, like and share posts, and follow other users. The API is built using Flask, MySQL, and JWT for authentication.

## Features

- **User Registration & Authentication**: Users can register, log in, and be authenticated using JWT tokens.
- **Post Management**: Users can create, update, and delete posts. Users can also view posts created by other users.
- **Comments**: Users can comment on posts. Comments are associated with both the post and the user who created them.
- **Likes**: Users can like posts. Each user can like a post only once.
- **Shares**: Users can share posts. Each share is associated with both the user and the post.
- **Follow System**: Users can follow other users. A user can follow another user only once and can unfollow them later.
- **Security**: Basic security features such as XSS prevention using `bleach` and password hashing.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **Raw Sql**
- **Security**: `bleach` for sanitizing inputs to prevent XSS attacks, password hashing with strong algorithms

## Prerequisites

Before running the project, make sure you have the following installed:

- **Docker** & **Docker Compose**
- **Python 3.9** or higher
- **MySQL**

## Project Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com//social-media-platform.git #TODO
   cd social-media-platform
   ```

2. **Set Up Environment Variables**:

   Create a `.env` file in the root directory and add the following:

   ```env
   MYSQL_USER=root
   MYSQL_PASSWORD=root
   MYSQL_HOST=db
   MYSQL_DB=newsfeed_db
   SECRET_KEY=a3b2c47f8bcae1234567abcd98ef1234567aa9b3cdef9b2345678aabbccddeee
   JWT_EXPIRATION=3600
   ```

3. **Build and Run with Docker Compose**:

   The project uses Docker Compose to manage the services for the API and the database.

   ```bash
   docker-compose up --build
   ```

   This will build and run the API and MySQL database in Docker containers.
4. ** **

## Database Setup

To set up the database schema, follow the steps below:

1. **Open MySQL terminal**:

   Depending on system, you can open the MySQL terminal by running:

   - For Windows (via Command Prompt or PowerShell):
     ```bash
     mysql -u root -p
     ```

   When prompted, enter your MySQL root password.

2. **Create the Database**:

   Inside the MySQL terminal, create the database for the project:
   ```sql
   CREATE DATABASE newsfeed_db;

   USE newsfeed_db;
   source /path/to/sql_schema.sql;


6. **Run Tests**:
   To run the tests, make sure the environment is running and then execute:

   ```bash
   pytest
   ```

## API Endpoints

### User Authentication
- **POST** `/register`: Register a new user.
- **POST** `/login`: Log in and get a JWT token.

### Posts
- **POST** `/post`: Create a new post (JWT required).
- **PUT** `/post/<int:post_id>`: Update an existing post (JWT required).
- **DELETE** `/post/<int:post_id>`: Delete a post (JWT required).
- **GET** `/post/<int:post_id>`: Get a post by its ID.

### Comments
- **POST** `/post/<int:post_id>/comment`
- **DELETE** `/comment/<int:comment_id>`

### Likes
- **POST** `/post/<int:post_id>/like`
- **DELETE** `/post/<int:post_id>/like`

### Shares
- **POST** `/post/<int:post_id>/share`

### Follow System
- **POST** `/user/<int:user_id>/follow`
- **DELETE** `/user/<int:user_id>/follow`