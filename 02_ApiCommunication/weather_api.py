import requests
import time

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


# API (weather)
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 19.07,
    "longitude": 72.87,
    "current_weather": True
}

result = make_api_request(url, params=params)

if result:
    weather = result.get("current_weather", {})
    print("Temperature:", weather.get("temperature"), "°C")
    print("Wind Speed:", weather.get("windspeed"), "km/h")