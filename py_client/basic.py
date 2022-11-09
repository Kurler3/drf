import requests
 
 
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint) # HTTP REQUEST

print(get_response.text) # PRINT RAW TEXT RESPONSE