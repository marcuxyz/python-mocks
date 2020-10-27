import json
import pytest


def open_json(filename):
    with open(f"{filename}", "r") as f:
        return json.loads(f.read())


@pytest.fixture
def books_mock():
    return open_json("data.json")