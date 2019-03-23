import requests
import json

url = 'http://pulse-rest-testing.herokuapp.com/books'

respons = requests.get('http://pulse-rest-testing.herokuapp.com/books' )
print(respons.content)
x = respons.json()
print(type(x))





#r = requests.post('http://pulse-rest-testing.herokuapp.com/books', data ={"title": "Somebok", "author": "Someauthor"})

r = requests.delete('http://pulse-rest-testing.herokuapp.com/books/43')