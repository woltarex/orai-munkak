listDays, listTemp = ['Hétfő', "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"], []
for i in range(7):
    listTemp.append(int(input(f'Add meg {listDays[i]} hőmérsékletét: ')))
varFagy, varFagyC, varAvg, listHom = False, 0, sum(listTemp), []
print(f'Napok átlaghőmérséklete: {varAvg/len(listTemp)}')
print(f'Legmelegebb nap: {(listTemp.index(max(listTemp)))+1}, hőmérséklete: {max(listTemp)}')
for i in listTemp:
    if i < 0:
        varFagy= True
        varFagyC += 1
print('Fagyott') if varFagy == True else print('Nem fagyott')
print(f'{varFagyC} napon fagyott')
for i in range(len(listTemp)):
    listHom.append(listDays[i]) if listTemp[i] > 15 else None
print(f'{", ".join(listHom)} napokon volt 15° feletti hőmérséklet')