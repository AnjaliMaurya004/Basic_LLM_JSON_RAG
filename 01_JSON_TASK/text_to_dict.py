data_dict = {}

with open("text.txt") as file:
    words = file.read().split()

for i in range(0, len(words), 2):
    key = words[i]
    value = words[i + 1]
    data_dict[key] = value

print(data_dict)