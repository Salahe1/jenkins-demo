import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the app
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        # Test the '/' route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello, Jenkins Pipeline!")

if __name__ == '__main__':
    unittest.main()
