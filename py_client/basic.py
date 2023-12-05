import requests

endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, params={"abc":123}, json={"name":"andoni"}) #Application programming interface

# print(get_response.text) #print raw response
# print(get_response.status_code)
# print(get_response.json())

post_response = requests.post(endpoint, json={"title": None, 'content':'Post TEST'})

# print(post_response.text) #print raw response
# print(post_response.status_code)
# print(post_response.json())