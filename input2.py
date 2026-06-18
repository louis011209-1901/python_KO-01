import requests

e = 2600000
n = 1200000

service = "https://geodesy.geo.admin.ch/reframe/lv95towgs84"

parameter = {"easting": e,
             "northing": n,
             "format": "json"}

response = requests.get(url=service, params=parameter, verify=False)
result = response.json()

print(result["easting"])
print(result["northing"])