with open("text1.txt", "r") as file:
    template = file.read()
data ={
    "name":"Anjali",
    "question": "What is the temperature today"
}
output = template.format(**data)
print(output)