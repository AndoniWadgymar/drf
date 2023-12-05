import requests

product_id = input("What Product do you want to delete?")

endpoint = f"http://localhost:8000/api/products/{product_id}/destroy/"

get_response = requests.delete(endpoint)
print(get_response.status_code)