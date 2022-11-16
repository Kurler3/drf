import requests
 
product_id = input("What is the product id you want to delete? \n")

try:
    product_id = int(product_id)
except:
    print('Product is is not valid')
    exit(1)

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

get_response = requests.delete(
        endpoint,
    ) # HTTP REQUEST

# PRINT STATUS CODE
print(get_response.status_code, get_response.status_code == 204)