import datetime

tag = int(input("Tag meiner Geburt (z.B. 1): "))
monat = int(input("Monat meiner Geburt (z.B. 12): "))
jahr = int(input("Jahr meiner Geburt (z.B. 2009): "))

geburt = datetime.date(jahr, monat, tag)

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

geburts_wochentag = wochentage[geburt.weekday()]
print("Ich wurde an einem", geburts_wochentag, "geboren.")

achtzehnter = datetime.date(jahr + 18, monat, tag)
achtzehnter_wochentag = wochentage[achtzehnter.weekday()]

zwanziger = datetime.date(jahr + 20, monat, tag)
zwanziger_wochentag = wochentage[zwanziger.weekday()]

dreissigster = datetime.date(jahr + 30, monat, tag)
dreissigster_wochentag = wochentage[dreissigster.weekday()]

vierzigster = datetime.date(jahr + 40, monat, tag)
vierzigster_wochentag = wochentage[vierzigster.weekday()]

fünfzigster = datetime.date(jahr + 50, monat, tag)
fünfzigster_wochentag = wochentage[fünfzigster.weekday()]

sechzigster = datetime.date(jahr + 60, monat, tag)
sechzigster_wochentag = wochentage[sechzigster.weekday()]

siebenundsechzigster = datetime.date(jahr + 67, monat, tag)
siebenundsechzigster_wochentag = wochentage[siebenundsechzigster.weekday()]

siebzigster = datetime.date(jahr + 70, monat, tag)
siebzigster_wochentag = wochentage[siebzigster.weekday()]

achzigster = datetime.date(jahr + 80, monat, tag)
achzigster_wochentag = wochentage[achzigster.weekday()]

neunzigster = datetime.date(jahr + 90, monat, tag)
neunzigster_wochentag = wochentage[neunzigster  .weekday()]

hundertster = datetime.date(jahr + 100, monat, tag)
hundertster_wochentag = wochentage[hundertster.weekday()]

print("Mein 18. Geburtstag fällt auf einen", achtzehnter_wochentag + ".")
print("Mein 20. Geburtstag fällt auf einen", zwanziger_wochentag + ".")
print("Mein 30. Geburtstag fällt auf einen", dreissigster_wochentag + ".")
print("Mein 40. Geburtstag fällt auf einen", vierzigster_wochentag + ".")
print("Mein 50. Geburtstag fällt auf einen", fünfzigster_wochentag + ".")
print("Mein 60. Geburtstag fällt auf einen", sechzigster_wochentag + ".")
print("Mein 67. Geburtstag fällt auf einen", siebenundsechzigster_wochentag + ".")
print("Mein 70. Geburtstag fällt auf einen", siebzigster_wochentag + ".")
print("Mein 80. Geburtstag fällt auf einen", achzigster_wochentag + ".")
print("Mein 90. Geburtstag fällt auf einen", neunzigster_wochentag + ".")
print("Mein 100. Geburtstag fällt auf einen", hundertster_wochentag + ".")