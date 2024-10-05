import unittest
from unittest.mock import patch, MagicMock
from services.post_service import PostService

class TestPostService(unittest.TestCase):

    @patch('services.post_service.get_db_connection')
    def test_create_post(self, mock_get_db_connection):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_connection.return_value = mock_conn

        # Define expected inputs
        user_id = 1
        content = "Test Post Content"

        # Define behavior of mock cursor
        mock_cursor.lastrowid = 10  # Simulating created post ID

        # Call the service method
        result, status_code = PostService.create_post(user_id, content)

        # Assert that the SQL query was executed
        mock_cursor.execute.assert_called_with("INSERT INTO Post (user_id, content) VALUES (%s, %s)", (user_id, content))
        mock_conn.commit.assert_called_once()  # Commit should be called once

        # Assert result and status code
        self.assertEqual(result['post_id'], 10)
        self.assertEqual(status_code, 201)

    @patch('services.post_service.get_db_connection')
    def test_update_post(self, mock_get_db_connection):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_connection.return_value = mock_conn

        # Define expected inputs
        post_id = 10
        content = "Updated Post Content"

        # Call the service method
        result, status_code = PostService.update_post(post_id, content)

        # Assert that the SQL query was executed
        mock_cursor.execute.assert_called_with("UPDATE Post SET content = %s WHERE id = %s", (content, post_id))
        mock_conn.commit.assert_called_once()

        # Assert result and status code
        self.assertEqual(result['message'], 'Post updated successfully')
        self.assertEqual(status_code, 200)

    @patch('services.post_service.get_db_connection')
    def test_delete_post(self, mock_get_db_connection):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_connection.return_value = mock_conn

        # Define expected input
        post_id = 10

        # Call the service method
        result, status_code = PostService.delete_post(post_id)

        # Assert that the SQL query was executed
        mock_cursor.execute.assert_called_with("DELETE FROM Post WHERE id = %s", (post_id,))
        mock_conn.commit.assert_called_once()

        # Assert result and status code
        self.assertEqual(result['message'], 'Post deleted successfully')
        self.assertEqual(status_code, 200)

    @patch('services.post_service.get_db_connection')
    def test_get_post(self, mock_get_db_connection):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_connection.return_value = mock_conn

        # Define expected inputs and outputs
        post_id = 10
        mock_cursor.fetchone.return_value = (10, 1, "Test Post Content", "2023-07-28 12:00:00")

        # Call the service method
        result, status_code = PostService.get_post(post_id)

        # Assert that the SQL query was executed
        mock_cursor.execute.assert_called_with("SELECT * FROM Post WHERE id = %s", (post_id,))

        # Assert result and status code
        self.assertEqual(result[0], 10)  # post_id should match
        self.assertEqual(status_code, 200)

    @patch('services.post_service.get_db_connection')
    def test_get_post_not_found(self, mock_get_db_connection):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_connection.return_value = mock_conn

        # Simulate no post found
        post_id = 999
        mock_cursor.fetchone.return_value = None

        # Call the service method
        result, status_code = PostService.get_post(post_id)

        # Assert that the SQL query was executed
        mock_cursor.execute.assert_called_with("SELECT * FROM Post WHERE id = %s", (post_id,))

        # Assert result and status code
        self.assertEqual(result['message'], 'Post not found')
        self.assertEqual(status_code, 404)

if __name__ == '__main__':
    unittest.main()
