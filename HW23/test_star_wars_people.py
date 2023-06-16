import pytest


@pytest.mark.parametrize('keyword, value', [('name', 'Luke Skywalker'), ('height', '172'), ('mass', '77')])
def test_check_person_1(people_service, keyword, value):
    responce = people_service.get_person(1)

    print(responce.json())
    assert responce.json()[keyword] == value


import requests
import pytest


# Test for GET request
def test_get_request():
    url = 'https://api.restful-api.dev/objects'
    response = requests.get(url)

    # Check response code
    assert response.status_code == 200

    # Check response body
    # Add assertions for the specific response body attributes if necessary


# Test for POST request
def test_post_request():
    url = 'https://api.restful-api.dev/objects'
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=data)

    # Check response code
    assert response.status_code == 201

    # Check response body
    # Add assertions for the specific response body attributes if necessary


# Test for PUT request
def test_put_request():
    url = 'https://api.restful-api.dev/objects/7'
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(url, json=data)

    # Check response code
    assert response.status_code == 200

    # Check response body
    # Add assertions for the specific response body attributes if necessary


# Test for PATCH request
def test_patch_request():
    url = 'https://api.restful-api.dev/objects/7'
    data = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(url, json=data)

    # Check response code
    assert response.status_code == 200

    # Check response body
    # Add assertions for the specific response body attributes if necessary


# Test for DELETE request
def test_delete_request():
    url = 'https://api.restful-api.dev/objects/6'
    response = requests.delete(url)

    # Check response code
    assert response.status_code == 200
