personen = ["Lionel Messi", "Cristiano Ronaldo", "Tim Payne", "Luka Vuskovic", "Gerd Müller", "Manuel Müller", "Ardon Jashari", "Michael Olise"]

with open("personen.txt", "w", encoding="utf-8") as f:
    for person in personen:
        f.write(person + "\n")

nachnamen = []

with open("personen.txt", "r", encoding="utf-8") as f:
    for zeile in f:
        zeile = zeile.strip()
        vorname, nachname = zeile.split(" ")
        nachnamen.append(nachname)
        print(nachname)

nachnamen.sort()

with open("nachnamen_alphabetisch.txt", "w", encoding="utf-8") as f:
    for name in nachnamen:
        f.write(name + "\n")