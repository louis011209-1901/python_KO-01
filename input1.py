import sys
user_param: str = sys.argv

i = 0
for a in sys.argv:
    print(f"Der Wert am Index {i} in sys.argv ist: {a}")
    i += 1