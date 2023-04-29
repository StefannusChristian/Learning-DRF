import requests

endpoint = "http://localhost:8000/api/"

# HTTP Request
get_response = requests.get(endpoint,params={"abc":123},json={"query":"Hello world"})
print(get_response.json())