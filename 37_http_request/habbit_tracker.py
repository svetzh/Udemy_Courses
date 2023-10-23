import requests
from datetime import datetime
#  https://pixe.la/v1/users/svetlio/graphs/graph1.html

USERNAME = "svetlio"
TOKEN = "y43ka3oh8wjb8xrkr0uk"
GRAPH_ID = "graph1"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
#
# past_day = datetime(year=2023, month=10, day=22)
#

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
print(response)


# del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{past_day.strftime(f'%Y%m%d')}"

# response = requests.delete(url=del_endpoint, headers=headers)
# print(response.text)