import requests

ort = "Bahnhofstrasse 1 8001 Zürich"

url = "https://api3.geo.admin.ch/rest/services/ech/SearchServer"

params = {
    "searchText": ort,
    "type": "locations"
}

response = requests.get(url, params=params)
data = response.json()

for result in data["results"]:
    attrs = result["attrs"]
    print(attrs["label"])
    print(attrs["lat"], attrs["lon"])