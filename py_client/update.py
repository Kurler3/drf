import requests
 
 
endpoint = "http://localhost:8000/api/products/3/update/"

get_response = requests.put(
        endpoint,
        json={
            "title": 'New title!! :D'
        }
    ) # HTTP REQUEST

print(get_response.json()) # PRINT RAW TEXT RESPONSE