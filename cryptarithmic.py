from itertools import permutations

letters = "T W O F U R".split()
digits = range(10)

for perm in permutations(digits, len(letters)):
    d = dict(zip(letters, perm))
    
    # Leading digit constraint
    if d['T'] == 0 or d['F'] == 0:
        continue
    
    # Construct numbers
    TWO = 100*d['T'] + 10*d['W'] + d['O']
    FOUR = 1000*d['F'] + 100*d['O'] + 10*d['U'] + d['R']
    
    if TWO + TWO == FOUR:
        print("Solution:", d)
        print(f"{TWO} + {TWO} = {FOUR}")
        break