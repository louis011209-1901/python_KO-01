o = float(input("Ostwert (E) eingeben: "))
n = float(input("Nordwert (N) eingeben: "))

o_formatiert = f"{o:,.0f}".replace(",", "'")
n_formatiert = f"{n:,.0f}".replace(",", "'")

print(f"E {o_formatiert} / N {n_formatiert}")

if 2480000 <= o <= 2840000 and 1070000 <= n <= 1300000:
    print("De Ponkt esch innerhalb vo de Schwiiz.")
else:
    print("De Ponkt esch osserhalb vo de Schwiiz.")