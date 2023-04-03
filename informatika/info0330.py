bolygo = ["Merkúr",
          "Vénusz",
          "Föld",
          "Mars",
          "Jupiter",
          "Szaturnusz",
          "Uránusz",
          "Neptunusz"]
hold = [0,0,1,2,63,62,27,13]
nulla = 0

for i in range(len(bolygo)):
    if hold[i] == 0:
        print(bolygo[i])
        nulla += 1

print(nulla)

legtobb = 0

for i in range(len(bolygo)):
    if hold[i] > hold[legtobb]:
        legtobb = i
print(bolygo[legtobb], hold[legtobb])

ossz = 0
for i in range(len(hold)):
    ossz += hold[i]

print(ossz/len(hold))

van= False
print("blabla: ", end='')
for i in range(len(bolygo)):
    if hold[i] >= 60:
        print(bolygo[i], hold[i], end=', ')
print(f'\nVan: {van}')