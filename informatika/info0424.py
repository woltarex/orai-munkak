import random
import string
nev = []
for i in range(6):
    nev.append(''.join(random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=4)))

cukorka = []

for i in range(len(nev)):
    cukorka.append(random.randint(1, 9))
print(nev)
print(cukorka)

extra=int(input("Extra cukorkák? "))

#print(nev[cukorka.index(max(cukorka))])

maxi = 0
for i in range(len(cukorka)):
    if cukorka[i] > cukorka[maxi]:
        maxi=i
print(f"{nev[maxi]}-nak/-nek van a legtöbb cukra: {cukorka[maxi]}")

van = False

for i in range(len(cukorka)):
    if cukorka[i] > 5:
        van = True
        
print(van)

osszeg = 0
for i in range(len(cukorka)):
    osszeg+=cukorka[i]
print(osszeg)