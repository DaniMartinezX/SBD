import requests

res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "9264bfb31e07de95718e90eb8ddcfc17593e677098491ff61ea06d2284eb6178"})

data = res.json()

print(data)
