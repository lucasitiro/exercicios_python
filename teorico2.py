a = int(input())
b = int(input())
c = int(input())
s = a+b+c
if (s < 35):
    d = a%2
elif (s < 52):
    d = b%3
elif (s < 65):
    d = c%4
else:
    d = 1
if (d > 1 or s > 60):
    e = a/b
else:
    e = b/a
f = a+c+d+e**2
print(s,d,e,f)