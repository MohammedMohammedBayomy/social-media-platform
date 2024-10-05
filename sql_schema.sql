-- Create the 'User' table
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,  -- Stores hashed passwords
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'Post' table
CREATE TABLE post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE  -- If user is deleted, delete their posts
);

-- Create the 'Comment' table
CREATE TABLE comment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES Post(id) ON DELETE CASCADE,  -- If post is deleted, delete comments
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE   -- If user is deleted, delete comments
);

-- Create the 'Like' table
CREATE TABLE like (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, post_id),  -- Ensure a user can like a post only once
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,  -- If user is deleted, remove their likes
    FOREIGN KEY (post_id) REFERENCES Post(id) ON DELETE CASCADE   -- If post is deleted, remove likes
);

-- Create the 'Share' table
CREATE TABLE share (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,  -- If user is deleted, remove shares
    FOREIGN KEY (post_id) REFERENCES Post(id) ON DELETE CASCADE   -- If post is deleted, remove shares
);

-- Create the 'Follow' table for user relationships
CREATE TABLE follow (
    id INT AUTO_INCREMENT PRIMARY KEY,
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (follower_id, followed_id),  -- Prevent duplicate follows
    FOREIGN KEY (follower_id) REFERENCES User(id) ON DELETE CASCADE,  -- If user is deleted, remove follows
    FOREIGN KEY (followed_id) REFERENCES User(id) ON DELETE CASCADE   -- If user is deleted, remove followers
);
