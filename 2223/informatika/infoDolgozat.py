import random
penz, osszes, felett = [random.randint(10000, 20000) for i in range(int(input("Hány tagja van a társaságnak? ")))], 0, 0
tobb, igaz = [felett for felett in penz if felett > 15000], [elem for elem in penz if elem > 18000]
kapott = True if igaz != [] else None
print(penz)
print(f"Átlagosan {sum(penz) / len(penz)} forintot kapnak az egyes tagok.")
print(f"{len(tobb)} tag kapott 15000 Ft feletti összeget.")
print(f"Ő kapta a legnagyobb összeget: {penz.index(max(penz)) + 1}, {max(penz)} forintot.")
print("Kapott valaki 18000 feletti összeget.") if kapott == True else print("Nem kapott senki 18000 feletti összeget.")