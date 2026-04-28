import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GITHUB_API_KEY")
print(api_key)
def make_api_request(url, method="GET", headers=None, params=None, data=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}")

            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=data,
                timeout=5
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                print("All retries failed")
                return None
            
#AUTH  API
url = "https://api.github.com/user"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/vnd.github+json"
}

result = make_api_request(url, headers=headers)

if result:
    print("Username:", result.get("login"))
    print("Public repos:", result.get("public_repos"))