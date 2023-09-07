# 1. feladat
db_gyerek = int(input('Hány gyerek van? '))

# 2. feladat
cukorkak = []
for i in range(db_gyerek):
    cukorkak.append(int(input(f'Hány cukorkája van a(z) {i+1}. gyereknek? ')))

# 3. feladat
db_extra = int(input('Hány db extra cukorkánk van? '))

# 4. feladat
cukorka_max = 0
cukorka_gyerek = 0
for i in range(len(cukorkak)):
    if cukorkak[i] > cukorka_max:
        cukorka_max = cukorkak[i]
        cukorka_gyerek = i
print(f'\nA(z) {cukorka_gyerek+1}. gyereknek volt a legtöbb cukra: {cukorka_max}\n')

# 5. feladat
cukorkak_legtobb = []
for i in range(len(cukorkak)):
    if cukorkak[i] + db_extra >= cukorka_max:
        print(f'A(z) {i+1}. gyereknek lenne a legtöbb cukra ({cukorkak[i]} + {db_extra} = {cukorkak[i] + db_extra})')
    else:
        print(f'A(z) {i+1}. gyereknek NEM lenne a legtöbb cukra ({cukorkak[i]} + {db_extra} = {cukorkak[i] + db_extra})')
