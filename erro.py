v = []
y = 0
soma = 0
n = int(input("Digite a quantidade de amostras:"))

for i in range(n):
    x = float(input("Digite o valor:"))
    v.append(x)
    y = y + x

media = y/n

for i in v:
    soma+= (media - i)**2

desvio = (1/(n*(n-1))*soma)**(1/2)

print(desvio)


