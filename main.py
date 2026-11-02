namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")

import random
tal = random.randint(1, 10)

Gissning = int(input("Gissa ett tal mellan 1 och 10: "))
if Gissning == tal:
    print(f"Rätt, det var {tal}")
else:
    print(f"Tyvärr det var {tal}")

slumptal = random.randint(1, 10)
i = 1
while i<= 3:
    gissning = int(input(f"Försök {i}: Gissa talet: "))
    if gissning == slumptal:
        print("Rätt Gissat!")
        break
    else:
        print("Fel gissat!")
    i += 1