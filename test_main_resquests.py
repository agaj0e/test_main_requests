import requests
import pytest

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "ne znayu kak nazvat",
        "body": "nu tipa post",

    }
    response = requests.post(url, json=data)
    assert response.status_code == 201


def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/66"
    data = {
        "title": "Updated post",
        "body": "obnovil post",
        "userId": 11
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated post"

def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200