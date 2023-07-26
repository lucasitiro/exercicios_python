def maior_primo(x):   
    if x<2:
        return False
    else:
           
        while not primo(x):
            x = x-1
        return x
        
           
        
def primo(x):
    a = x-1
    while a>1:
        if x%a!=0:
            a = a-1    
        else:
            return False
    return True

        



        
            




