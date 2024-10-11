def factors(n):
    fac=[]
    i=2
    while i**2<=n:
        while n%i==0:
            n=n//i
            fac.append(i)
        i+=1
    if len(fac)==0:
        fac=[1,n]
        return fac
    else:
        return fac
print(factors(int(input())))


