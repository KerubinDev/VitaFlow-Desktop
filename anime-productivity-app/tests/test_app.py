import unittest
from gui.login import Login
from gui.dashboard import Dashboard
from utils.authentication import hash_password, verify_password
from database.connection import create_connection

class TestApp(unittest.TestCase):

    def setUp(self):
        self.connection = create_connection('test_database.db')
        self.login = Login()
        self.dashboard = Dashboard()

    def test_hash_password(self):
        password = "test_password"
        hashed = hash_password(password)
        self.assertNotEqual(password, hashed)
        self.assertTrue(verify_password(password, hashed))

    def test_login_valid_user(self):
        self.login.username = "valid_user"
        self.login.password = "valid_password"
        result = self.login.validate_user()
        self.assertTrue(result)

    def test_login_invalid_user(self):
        self.login.username = "invalid_user"
        self.login.password = "invalid_password"
        result = self.login.validate_user()
        self.assertFalse(result)

    def test_dashboard_progress(self):
        self.dashboard.load_user_data("valid_user")
        progress = self.dashboard.get_progress()
        self.assertIsInstance(progress, dict)

    def tearDown(self):
        self.connection.close()

if __name__ == '__main__':
    unittest.main()