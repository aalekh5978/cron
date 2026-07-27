import requests

URL = "https://sastasamaan.is-best.net/?wp_automatic=cron&id=11"

try:
    response = requests.get(URL, timeout=30)
    print(f"Status: {response.status_code}")
    print(response.text[:500])
except Exception as e:
    print(f"Error: {e}")
