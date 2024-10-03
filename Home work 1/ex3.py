def gcd(a, b):

    if b==0:
        return (1, 0, a)
    y, x, d = gcd(b, a % b)
    return (x, y - (a // b) * x, d)


s=list(map(int,input().split()))
a=s[0]
b=s[1]
x,y,d=gcd(a,b)
print(f"{x} {y} {d}")