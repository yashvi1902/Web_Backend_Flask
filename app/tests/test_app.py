import unittest
from app import create_app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_login(self):
        response = self.client.post('/login', json={'username': 'Yashvi', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
