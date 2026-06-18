import requests
import math

e_wgs = 7.452
n_wgs = 46.928

e_lv = 2600052
n_lv = 1198762

service = "https://geodesy.geo.admin.ch/reframe/wgs84tolv95"

parameter = {
    "easting": e_wgs,
    "northing": n_wgs,
    "format": "json"
}

response = requests.get(url=service, params=parameter, verify=False)
result = response.json()

swisstopo_e = float(result["easting"])
swisstopo_n = float(result["northing"])

print(f"swisstopo LV95: {swisstopo_e:.3f}, {swisstopo_n:.3f}")

dx = e_lv - swisstopo_e
dy = n_lv - swisstopo_n

distanz = math.sqrt(dx**2 + dy**2)

distanz_10m = round(distanz / 10) * 10

print(f"Distanz: {distanz:.2f} m")
print(f"Gerundet auf 10 m: {distanz_10m:.0f} m")