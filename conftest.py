import pytest
import requests

@pytest.fixture(scope='session')
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/books"

@pytest.fixture
def book(base_url):
    book_data = {"title": "New Book",
                 "author": "New Author"}
    yield book_data
    if id in book_data:
        requests.delete(f"{base_url}/books{book_data['id']}")