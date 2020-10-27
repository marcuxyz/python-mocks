import requests
import responses

from app import filter_books_by_pages

URL = "https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f"

@responses.activate
def test_filter_books_by_pages(books_mock):
    responses.add(responses.GET, URL, json=books_mock)
    response = requests.get(URL)

    results = filter_books_by_pages(response.json()["books"])
    assert len(results) == 4
