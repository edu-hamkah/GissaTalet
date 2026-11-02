lista = ["1. Oslo", "2. Stockholm", "3. Köpenhamn"]
svar = 1
print("Vilken huvudstad har Norge?")
print(lista[0])
print(lista[1])
print(lista[2])
gissning = int(input("Ditt val: "))
if gissning == svar:
    print("Rätt")
else:
    print("Fel, rätt svar var Oslo")

