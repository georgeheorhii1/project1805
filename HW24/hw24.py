import requests
import psycopg2


class Adapter:
    def __init__(self, api_endpoint, db_params):
        self.api_endpoint = api_endpoint
        self.db_params = db_params

    def transfer_api_to_db(self, method, path, data=None):
        response = requests.request(method, self.api_endpoint + path, json=data)
        if response.status_code == 201:
            record_id = response.json()['id']
            self._insert_record(record_id)
            return record_id
        return None

    def transfer_db_to_api(self, record_id, method, path, data=None):
        self._update_record(record_id)
        response = requests.request(method, self.api_endpoint + path, json=data)
        if response.status_code == 200:
            return response.json()
        return None

    def _insert_record(self, record_id):
        conn = psycopg2.connect(**self.db_params)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (record_id) VALUES (%s)", (record_id,))
        conn.commit()
        conn.close()

    def _update_record(self, record_id):
        conn = psycopg2.connect(**self.db_params)
        cursor = conn.cursor()
        cursor.execute("UPDATE records SET record_id = %s", (record_id,))
        conn.commit()
        conn.close()

    def check_record_exists(self, record_id):
        conn = psycopg2.connect(**self.db_params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE record_id = %s", (record_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None


api_endpoint = 'https://restful-api.dev/'
db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password'
}

adapter = Adapter(api_endpoint, db_params)

api_data = {'name': 'John', 'age': 25}
record_id = adapter.transfer_api_to_db('POST', '/objects', data=api_data)
assert record_id is not None
assert adapter.check_record_exists(record_id)

db_data = {'name': 'Jane', 'age': 30}
response = adapter.transfer_db_to_api(record_id, 'PUT', f'/objects/{record_id}', data=db_data)
assert response is not None
assert response['name'] == db_data['name']
assert response['age'] == db_data['age']

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()
cursor.execute("DELETE FROM records WHERE record_id = %s", (record_id,))
conn.commit()
conn.close()
