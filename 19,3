import requests

response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
print(response.json())



import requests

data = {
    "id": 444555,
    "name": "Major",
    "status": "available"
}
response = requests.post("https://petstore.swagger.io/v2/pet", json=data)
print(response.json())



import requests

pet_id = 444555
response = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
print(response.json())

import requests

pet_id = 444555
data = {
    "id": pet_id,
    "name": "Major",
    "status": "sold"
}
response = requests.put(f"https://petstore.swagger.io/v2/pet/{pet_id}", json=data)
print(response.json())
