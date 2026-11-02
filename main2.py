lista = ["1. Oslo", "2. Stockholm", "3. Köpenhamn"]
rätt = 2
print("Vilken huvudstad har Sverige?")
print(lista[0])
print(lista[1])
print(lista[2])
gissning = int(input("Ditt val: "))
if gissning == rätt:
    print("Rätt")