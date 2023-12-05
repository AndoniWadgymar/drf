import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint) #Application programming interface
print(get_response.text) #print raw response
print(get_response.status_code)
print(get_response.json())