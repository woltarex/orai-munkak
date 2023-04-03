import random
listNev = ['Álmos', 'Előd', 'Ond', 'Kond', 'Tas', 'Huba']

listSuly = []

for varI in range(len(listNev)):
    listSuly.append(random.randint(50, 120))

print(listSuly)

varOssz = 0

for varI in listSuly:
    varOssz += int(varI)

print(f'Átlagtömeg: {round(varOssz / len(listNev), 2)}')

dictNev = {listNev[0]:listSuly[0],
           listNev[1]:listSuly[1],
           listNev[2]:listSuly[2],
           listNev[3]:listSuly[3],
           listNev[4]:listSuly[4],
           listNev[5]:listSuly[5],}

varMin = min(dictNev, key=dictNev.get)

print(f'{varMin} {dictNev[varMin]}')

varMin2 = 0
for varI in range(len(listSuly)):
    if listSuly[varI]<listSuly[varMin2]:
        varMin2 = varI
print(f'{listNev[varMin2]} a legsoványabb, {listSuly[varMin2]} kg')

varVan = False
for varI in range(len(listSuly)):
    if listSuly[varI] >= 100 and listSuly[varI] <= 120:
        varVan = True
if varVan == True:
    print('Van 100 és 120 közötti súly.')
else:
    print('Nincs 100 és 120 közötti súly.')

listOver100 = []

print('100 kg fölöttiek: ', end='')
for i in range(len(listSuly)):
    if listSuly[i] > 100:
        listOver100.append(listNev[i])
    
print(*listOver100, sep=', ')

varDb = 0
for i in range(len(listSuly)):
    if listSuly[i]>80:
        varDb+=1
print(f'80 kg fölöttiek száma {varDb}')

i = 0
while listSuly[i]<80:
    i+=1
print(f'Az első 80 kg-t elérő egyén: {listNev[i]}')