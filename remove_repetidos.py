def remove_repetidos(lista):
    v = []
    for i in lista:
        if i not in v:
            v.append(i)
    v.sort()
    print(v)
    return v
    

                
        
                
        


