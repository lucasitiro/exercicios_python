v = [3,4,9,4,3]
def calc(v):
    f = 0
    g = 1
    for i in range(len(v)):
        f = f+v[i]
        g = g*v[i]
        if(f>18):
            v[0] = v[1]+v[2]
            break
        elif(f>15):
            v[1]=v[2]+v[3]
            break
        elif(f>12):
            v[2]=v[3]+v[4]
    print(f,g,v[0],v[1],v[2])
calc(v)
    