def root(n):
    if n//10==0:
        return n
    summa=n%10
    while n//10!=0:
        n=n//10
        summa += n % 10
    n=summa
    return root(n)
a=list(map(int,input().split()))
b=[0 for i in range(len(a))]
for i in range(len(a)):
    b[i]=root(a[i])
def merge(A, B):
    len_a = len(A)
    len_b = len(B)
    C = []
    i = 0
    j = 0
    while i < len_a or j < len_b:
        if i >= len_a:
            C.append(B[j])
            j += 1
            continue
        if j >= len_b:
            C.append(A[i])
            i += 1
            continue

        if root(A[i]) < root(B[j]):
            C.append(A[i])
            i += 1
        elif root(A[i])>root(B[j]):
            C.append(B[j])
            j += 1
        else:
            if A[i]<B[j]:
                C.append(A[i])
                i+=1
            else:
                C.append(B[j])
                j+=1
    return C
def merge_sort(arr):
    N = len(arr)
    if N == 1:
        return arr

    ind = N//2
    L = arr[0:ind]
    R = arr[ind:]
    return merge(merge_sort(L), merge_sort(R))

print(*merge_sort(a))

