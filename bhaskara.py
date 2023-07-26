import math

a = float(input("Digite  o valor de a:"))
b = float(input("Digite  o valor de b:"))
c = float(input("Digite  o valor de c:"))

d = (a+b+c)/3

z = (d-a)**2
y = (d-b)**2                  
c = (d-c)**2
h = math.sqrt(z+y+c)
u = math.sqrt(6)

incerteza = h/u

print(incerteza)

