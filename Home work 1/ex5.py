import numpy as np
n=4
m=4
a=np.array([[0 for i in range(m)]for j in range(n)])
c=0
startx=0
starty=0
finx=m-1
finy=n-1
a[0][0]=1

while c <= n * m:
    x = startx
    y = starty
    for x in range(startx, finx + 1):
        a[y][x] = c
        c+=1
    starty+=1
    if c<= n * m:
        for y in range(starty, finy + 1):
            a[y][x] = c
            c+=1
        finx-= 1
    if c <= n * m:
        for x in range(finx, startx - 1, -1):
            a[y][x] = c
            c+=1
        starty-=1
    if c <= n * m:
        for y in range(finy, starty - 1, -1):
            a[y][x] = c
            c+=1
        startx+=1
print(a)