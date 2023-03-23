import random
listNev = ['Álmos', 'Előd', 'Ond', 'Kond', 'Tas', 'Huba']

listSuly = []

for i in range(len(listNev)):
    listSuly.append(random.randint(50, 120))

print(listSuly)

varOssz = 0

for i in listSuly:
    varOssz += int(i)

print(f'Átlagtömeg: {round(varOssz / len(listNev), 2)}')

dictNev = {listNev[0]:listSuly[0],
           listNev[1]:listSuly[1],
           listNev[2]:listSuly[2],
           listNev[3]:listSuly[3],
           listNev[4]:listSuly[4],
           listNev[5]:listSuly[5],}

varMin = min(dictNev, key=dictNev.get)

print(f'{varMin} {dictNev[varMin]}')