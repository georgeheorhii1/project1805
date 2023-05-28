import requests
import json


class RandomDataAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def call_api_and_save_to_file(self, endpoint, filename):
        response = requests.get(f"{self.base_url}/{endpoint}")

        if response.status_code == 200:
            with open(filename, 'w') as file:
                json.dump(response.json(), file)
                print(f"JSON data saved to {filename}")
        else:
            print(f"API request failed with status code: {response.status_code}")


api = RandomDataAPI("https://random-data-api.com/api")
api.call_api_and_save_to_file("restaurant/random_restaurant", "random_restaurant.json")
