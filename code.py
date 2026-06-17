for zahl in [4, 4.5, 5, 5.5, 6]:
    rest = zahl % 2
    if rest == 0:
        print(zahl, "ist eine gerade Zahl")
    elif rest == 1:
        print(zahl, "ist eine ungerade Zahl")
    else:
        print(zahl, "ist eine Kommazahl")