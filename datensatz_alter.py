import datetime

def main():
    eingabe = input("Bitte Aufnahmedatum eingeben (TT.MM.JJJJ): ")

    try:
        tag, monat, jahr = map(int, eingabe.split("."))
        aufnahme_datum = datetime.date(jahr, monat, tag)

        heute = datetime.date.today()

        differenz = heute - aufnahme_datum
        tage_alt = differenz.days

        print(f"\nDer Datensatz ist {tage_alt} Tage alt.")

        if tage_alt > 365:
            print("Achtung: Datensatz ist älter als 1 Jahr – bitte auf Aktualität prüfen.")

    except ValueError:
        print("Ungültige Eingabe! Bitte das Datum im Format TT.MM.JJJJ eingeben (z.B. 01.12.2009).")

if __name__ == "__main__":
    main()