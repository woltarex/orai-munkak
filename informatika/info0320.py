import random

listKutya = []

for i in range(101):
    listKutya.append(random.randint(16,32))

print(listKutya)

varNosteny = 0
varHim = 0

for bloki in listKutya:
    if bloki >= 16 and bloki <=24:
        varNosteny += 1
    else:
        varHim += 1

print(f"Nőstények száma: {varNosteny}\nHímek száma: {varHim}")

varMax = max(listKutya)
print(varMax)