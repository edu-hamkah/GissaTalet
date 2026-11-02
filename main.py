namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")

import random
tal = random.randint(1, 10)

i = 1
while i<= 3:
    gissning = int(input(f"Försök {i}: Gissa talet: "))
    if gissning == tal:
        print("Rätt Gissat!")
        break
    else:
        print("Fel gissat!")
    i += 1