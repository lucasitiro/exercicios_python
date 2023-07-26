a = True
n = int(input("Digite o valor de n:"))
x = n
if n<0:
    a = False
elif n ==0:
    n = 1
    print(n)
else:
    while x>1:
        x = x-1
        n = n*x
    print(n)


