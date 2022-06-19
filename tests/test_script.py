import unittest

from main import main
import os


class TestToPerform(unittest.TestCase):
    def setUp(self):
        self.main = main.test_client()

    def tearDown(self):
        pass

    def test_page(self):
        response = self.main.get('/', follow_redirects=True)
        print(response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
