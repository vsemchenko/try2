import unittest
import requests


class Testclass1(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/books'
        self.book_id = 0

    def test_book_created(self):
        book_data = ('title' : 'New book',
                     'author': 'New author')

respons = requests.post(self.base_url, data=book_data)
self.assertEqual(201, respons.status_code)
self.assertEqual(body.get('title')book_data.get('title'))
body = respons.json()
self.book_id = body["id"]

    def tearDown(self):
        if self.book_id is not None:
            requests.delete(f"(self.base_url)(self.book_id)")


