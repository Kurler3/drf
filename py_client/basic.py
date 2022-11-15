import requests
 
 
endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(
        endpoint,
    ) # HTTP REQUEST

print(get_response.json()) # PRINT RAW TEXT RESPONSE