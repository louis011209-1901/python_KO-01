import random

def lottoziehung():
    zahlen = set(random.sample(range(1, 43), 6))
    zusatzzahl = random.randint(1, 6)
    return zahlen, zusatzzahl

def main():
    tipps = set(map(int, input("Gib 6 Zahlen ein (1–42): ").split()))
    tipp_zusatzzahl = int(input("Zusatzzahl (1–6): "))

    versuche = 0

    vier_richtig = 0
    vier_plus = 0
    fuenf_richtig = 0
    fuenf_plus = 0
    sechs_richtig = 0
    jackpot = 0

    while True:
        versuche += 1
        ziehung, zusatzzahl = lottoziehung()

        treffer = len(tipps & ziehung)
        
        if treffer == 4:
            vier_richtig += 1

            if zusatzzahl == tipp_zusatzzahl:
                vier_plus += 1

        if treffer == 5:
            fuenf_richtig += 1

            if zusatzzahl == tipp_zusatzzahl:
                fuenf_plus += 1

        elif treffer == 6:
            sechs_richtig += 1

            if zusatzzahl == tipp_zusatzzahl:
                jackpot += 1
                print("🎉 JACKPOT nach", versuche, "Versuchen!")
                break

    print("\n--- Ergebnis ---")
    print("Versuche total:", versuche)
    print("4 Richtige:", vier_richtig)
    print("4 Richtige + Zusatzzahl:", vier_plus)
    print("5 Richtige:", fuenf_richtig)
    print("5 Richtige + Zusatzzahl:", fuenf_plus)
    print("6 Richtige:", sechs_richtig)
    print("6 + Zusatzzahl (Jackpot):", jackpot)

main()