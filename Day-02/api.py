import requests
#call API
response = requests.get("https://randomuser.me/api/")

#convert to JSON
data = response.json()

#Extract data
user = data["results"][0]

print("Name:", user["name"]["first"])
print("Email:", user["email"])
print("Country:", user["location"]["country"])
                  