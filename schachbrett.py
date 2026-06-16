# Schachbrett
import string
buchstaben = string.ascii_lowercase[:8]
for i in range(8, 0, -1):
    for j in buchstaben:
        print(f"{j}{i}", end=" ")
    print()