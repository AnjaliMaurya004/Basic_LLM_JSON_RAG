import httpx
import asyncio
import time

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2"
]

async def fetch(client, url):
    response = await client.get(url)
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        return await asyncio.gather(*tasks)

start = time.time()

results = asyncio.run(main())

end = time.time()

print("Async Results:", results)
print("Async Time:", end - start)