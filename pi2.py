N = 5
x = []
y = []
for i in range(N):
    x.append(int(input()))

for i in range(N):
    y.append(int(input()))

z = []
f = 0
g = 0

for i in range(len(x)):
    if (i%2==0):
        z.append(x[i]+y[i])
    else:
        z.append(x[i]*y[i])
    f = f+x[i]
    g = g+y[i]
print(f,g,z[0],z[1],z[2],z[3],z[4])

