import requests

responce_example = requests.get('http://randomuser.me/api/')
assert responce_example.status_code == 200

print(responce_example.json())



