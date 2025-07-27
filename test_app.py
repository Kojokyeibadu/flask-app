import unittest
from app import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello from Flask App!')

if __name__ == '__main__':
    unittest.main()

Save by pressing `Ctrl+O`, `Enter`, then exit with `Ctrl+X`.
