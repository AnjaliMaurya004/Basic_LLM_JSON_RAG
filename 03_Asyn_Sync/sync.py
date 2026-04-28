import requests
import time

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2"
]

def fetch(url):
    response = requests.get(url)
    return response.json()

start = time.time()

results = []
for url in urls:
    results.append(fetch(url))

end = time.time()

print("Sync Results:", results)
print("Sync Time:", end - start)