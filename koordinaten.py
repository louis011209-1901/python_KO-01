from pyproj import Transformer
import math

transformer = Transformer.from_crs("EPSG:4326", "EPSG:2056", always_xy=True)

print("=== Punkt 1 (WGS84) ===")
lat1 = float(input("Breitengrad (lat): "))
lon1 = float(input("Längengrad (lon): "))

print("\n=== Punkt 2 (LV95) ===")
E2 = float(input("Ostwert E (m): "))
N2 = float(input("Nordwert N (m): "))

E1, N1 = transformer.transform(lon1, lat1)

print("\n=== Transformierter Punkt 1 (LV95) ===")
print(f"E1 = {E1:.2f} m")
print(f"N1 = {N1:.2f} m")

dE = E2 - E1
dN = N2 - N1

distance = math.sqrt(dE**2 + dN**2)

print("\n=== Ergebnis ===")
print(f"ΔE = {dE:.2f} m")
print(f"ΔN = {dN:.2f} m")

print(f"Distanz = {distance:.2f} m")
print(f"Distanz = {distance/1000:.3f} km")

print(f"Gerundet (10 m): {round(distance / 10) * 10} m")