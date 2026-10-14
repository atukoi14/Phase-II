import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    user = data[0] 

    name = user['name']
    profession = user['company']['name']
    email = user['email']
    city = user['address']['city']

print()
print("==== Employee Data ====")
print(f"Name  : {name}")
print(f"Profession: {profession}")
print(f"Email : {email}")
print(f"City  : {city}")