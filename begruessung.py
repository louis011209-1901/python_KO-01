def nameneingabe():
    while True:
        name = input("Bitte einen Nutzernamen eingeben: ").strip()
        if name == "":
            print("Ungültige Eingabe. Gib bitte einen Namen ein.")
        if any(char.isdigit() for char in name):
            print("Ungültig: Der Name darf keine Zahlen enthalten.")
        break

    if name.startswith(("A", "Ä", "a", "ä")):
        print("Toll. Du bist im Alphabet ganz vorn")

    print("Schleife ist fertig")
    return name


def begruessung(name):
    print(f"Hallo {name}")


name = nameneingabe()
begruessung(name)