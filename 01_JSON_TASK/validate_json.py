import json

try:
    with open("text_to_schema.json", "r") as f:
        data = json.load(f)  
    print("JSON is valid")
    print(data)

except json.JSONDecodeError as e:
    print("Invalid JSON")
    print("Error:", e)

except FileNotFoundError:
    print("File not found")