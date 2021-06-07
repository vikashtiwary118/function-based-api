import requests
import json

url = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=url, headers=headers, data=json_data)

    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Snal',
        'roll': 155,
        'city': 'Dhanbad'
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}

    r = requests.post(url, headers=headers,data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 2,
        'name': 'Mohit',
        'city': 'Dhanbad'
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}

    r = requests.put(url, headers=headers, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}

    r = requests.delete(url, headers=headers, data=json_data)
    data = r.json()
    print(data)


delete_data()
#update_data()
#post_data()


#get_data(id=1)
