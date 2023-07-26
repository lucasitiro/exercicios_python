x = int(input("Digite um número inteiro:"))
a = x
c = x
b = 0
while c>=1:
    a = a%10
    b = b+a
    c = c//10
    a = c
    if c<10:
        b = b+c
        break
print(b)

