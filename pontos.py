x = int(input("Digite um número"))
y = int(input("Digite outro número"))
a = int(input("Digite mais um número"))
b = int(input("Digite outro número"))
import math
d = math.sqrt(((x-a)**2)+((y-b)**2))
if d>=10:
    print("longe")
else:
     print("perto")