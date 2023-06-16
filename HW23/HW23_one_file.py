import requests


def create_object():
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
    respoce_json = response.json()
    return respoce_json['id'], response.status_code, response, respoce_json['createdAt']


# ok
def test_get_request():
    object_id, status_code, responce, updated_at = create_object()
    url = f'https://api.restful-api.dev/objects/{object_id}'
    response = requests.get(url)

    assert response.status_code == 200


def test_post_request():
    object_id, status_code, responce, updated_at = create_object()

    assert status_code == 200


# ok
def test_put_request():
    object_id, status_code, responce, updated_at = create_object()
    url = f'https://api.restful-api.dev/objects/{object_id}'
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

    assert response.status_code == 200

    assert response.json()['id'] == object_id


# ok
def test_patch_request():
    object_id, status_code, responce, updated_at = create_object()
    url = f'https://api.restful-api.dev/objects/{object_id}'
    data = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(url, json=data)

    assert response.status_code == 200

    assert response.json()['name'] == data['name']


def test_delete_request():
    object_id, status_code, responce, updated_at = create_object()
    url = f'https://api.restful-api.dev/objects/{object_id}'
    response = requests.delete(url)

    assert response.status_code == 200
