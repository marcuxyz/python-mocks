from app import filter_books_by_pages
import json
import requests
import responses

URL = "https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f"
file = open("data.json", "r")
books = json.loads(file.read())

@responses.activate
def test_filter_books_by_pages():
    responses.add(responses.GET, URL, json=books)
    response = requests.get(URL)

    results = filter_books_by_pages(response.json()["books"])
    assert len(results) == 4

file.close()