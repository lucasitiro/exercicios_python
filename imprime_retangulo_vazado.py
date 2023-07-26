x = int(input("digite a largura:"))
y = int(input("digite a altura:"))

if x<=2 and y<=2:
    for i in range(y):
        for j in range(x):
            print("#",end="")
        print()
else:
    for i in range(x):
        print("#",end="")
    print()
    for j in range(y-2):
        print("#",end="")
        for j in range(y-2):
            for t in range(x-2):
                print(" ",end="")
            print("#")
            break
        
    for i in range(x):
        print("#",end="")
    print()

    



      



   

