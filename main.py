namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")

import random
tal = random.randint(1, 10)
Gissning = input("Gissa ett tal mellan 1 och 10: ")
if Gissning == tal:
    print(f"Rätt, det var {tal}")
else:
    print(f"Tyvärr det var {tal}")