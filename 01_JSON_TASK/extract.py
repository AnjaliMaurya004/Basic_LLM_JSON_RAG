import json

with open("user_data.json", "r") as file:
    users = json.load(file)

print(users[0]["skill"][0])
