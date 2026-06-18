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

gdf_wgs84 = gdf.to_crs("EPSG:4326")

mitte = gdf_wgs84.geometry.union_all().centroid

karte = folium.Map(
    location=[mitte.y, mitte.x],
    zoom_start=10,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",
    attr="swisstopo"
)

for _, row in gdf_wgs84.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=f"{row['name']}: {row['hoehe']} m.ü.M."
    ).add_to(karte)

karte.save("messpunkte.html")

webbrowser.open("messpunkte.html")

print("Karte gespeichert: messpunkte.html")