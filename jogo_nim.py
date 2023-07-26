def computador_escolhe_jogada(n,m):
    l = 0
    a = 0
    if m==1:
        a = 1
    else:
        if n%(m+1)>m:
            a = m
        else:
            a = n%(m+1)
    if a>1:
        print("O computador tirou",a,"peças do tabuleiro.")
    if a==1:
        print("O computador tirou uma peça do tabuleiro.")
        
        
    if (n-a)>1:
        print("Agora restam",n-a,"peças no tabuleiro.")
    if (n-a)==1:
        print("Agora resta apenas uma peça no tabuleiro.")
    
    return a
def usuario_escolhe_jogada(n,m):
    
    x = int(input("Quantas peças você vai tirar?"))
    while x>m or x<1:
        x = int(input("Oops! Jogada inválida! Tente de novo."))     
    if x>1:
        print("Você tirou",x,"peças do tabuleiro.")
    if x==1:
        print("Você tirou uma peça do tabuleiro.")
        
        
    if (n-x)>1:
        print("Agora restam",n-x,"peças no tabuleiro.")
    if (n-x)==1:
        print("Agora resta apenas uma peça no tabuleiro.")
    return x
def partida():
    con = 0
    n = int(input("Quantas peças?"))
    while n<1:
        n = int(input("Oops, digite um número maior que um")) 
    m = int(input("Limites de peças por jogada?"))
    while m>n:
        m = int(input("Ops, o número de peças precisa ser maior que limite de peças por jogada!"))
    if n%(m+1)==0:
            print()
            print("Você começa!")
            x = usuario_escolhe_jogada(n,m)
            print()
            n=n-x
            con = 0
    else:
            print()
            print("Computador começa!")
            a = computador_escolhe_jogada(n,m)
            print()
            n=n-a
            con = 1
    while n>0:
        if con==0:
            a = computador_escolhe_jogada(n,m)
            print()
            n = n-a
            con = 1
            if n<= 0:
                print("Fim do jogo! O computador ganhou!")
                print()
                return 1

        else:
            x = usuario_escolhe_jogada(n,m)
            print()
            n = n-x
            con = 0
            if n<=0:
                print("Fim do jogo! Você ganhou!")
                print()
                return 2
    
        
def main():
        p = 1
        k = 0
        l = 0
        
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print()
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato 2")
        j = int((input()))
        if j==1:
            print("Você escolheu uma partida isolada!")
            partida()
        if j==2:
            print("Voce escolheu um campeonato!")
            while p<=3:
                print("**** Rodada",p," ****")
                x = partida()
                if x==1:
                    l=l+1
                if x==2:
                    k = k+1
                p=p+1
            print("**** Final do campeonato! ****")
            print("Placar: Você",k,"X",l," Computador")
main()











    
        
    





