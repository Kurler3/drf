import requests

endpoint1 = "https://httpbin.org/status/200"
endpoint2 = "https://httpbin.org/anything"



get_response = requests.get(endpoint2) # HTTP REQUEST

print(get_response.text) # PRINT RAW TEXT RESPONSE