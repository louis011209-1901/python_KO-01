import pandas as pd
import geopandas as gpd
import folium
import webbrowser

df = pd.read_csv("messpunkte.csv")

gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["ost"], df["nord"]),
    crs="EPSG:2056"
)

zonen = gpd.read_file("messgebiete.geojson")

zonen = zonen.to_crs(gdf.crs)

result = gpd.sjoin(
    gdf,
    zonen,
    how="left",
    predicate="within"
)

print("Punkte ohne Zone:")

ohne_zone = result[result["index_right"].isna()]

if len(ohne_zone) == 0:
    print("Alle Punkte wurden einer Zone zugeordnet.")
else:
    for _, row in ohne_zone.iterrows():
        print(row["name"])

gdf_wgs84 = gdf.to_crs("EPSG:4326")
zonen_wgs84 = zonen.to_crs("EPSG:4326")

mitte = gdf_wgs84.geometry.union_all().centroid

karte = folium.Map(
    location=[mitte.y, mitte.x],
    zoom_start=10,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",
    attr="swisstopo"
)

farben = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "brown",
    "darkred",
    "cadetblue"
]

for i, (_, zone) in enumerate(zonen_wgs84.iterrows()):
    farbe = farben[i % len(farben)]

    folium.GeoJson(
        zone.geometry,
        style_function=lambda feature, f=farbe: {
            "fillColor": f,
            "color": f,
            "weight": 2,
            "fillOpacity": 0.3
        },
        tooltip=zone.get("name", f"Zone {i+1}")
    ).add_to(karte)

for _, row in gdf_wgs84.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=f"{row['name']}: {row['hoehe']} m.ü.M."
    ).add_to(karte)

karte.save("messpunkte_zonen.html")

webbrowser.open("messpunkte_zonen.html")

print("Karte gespeichert: messpunkte_zonen.html")