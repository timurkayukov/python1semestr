def search(a,h):
    for i in range(len(a)-1,-1,-1):
        if a[i]>=h:
            return i
    return -1
def beauty(a):
    b=[-1 for i in range(len(a))]
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            b[i]=-1
            maximum=a[i]
        else:
            b[i]=search(a[:i],a[i])

    return b
a=list(map(int,input().split()))
print(*beauty(a))




