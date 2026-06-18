import math

def check_r():
    while True:
        try:
            r = float(input("Bitte gib den Radius des Kreises ein: "))
            if r <= 0:
                raise Exception("Radius darf nicht negativ sein. Gib bitte einen positiven Wert ein.")
            break
        except ValueError:
            print("Ungültige Eingabe. Gib bitte eine Zahl ein.")
        except Exception:
            print("Radius darf nicht negativ sein. Gib bitte einen positiven Wert ein.")
    print("Die While-Schleife ist fertig.")
    return r
def flaeche(r):
    return r**2 * math.pi

def umfang(r):
    return 2 * math.pi * r

def calc_diameter(r):
    return 2 * r


r = check_r()
A = flaeche(r)

print(f"Die Fläche vom Kreis ist: {A}")