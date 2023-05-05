import requests

endpoint = "http://localhost:8000/api/"

# HTTP Request
get_response = requests.post(endpoint,json={"title":"hi","content":"hello","price":"abc"})
print(get_response.json())