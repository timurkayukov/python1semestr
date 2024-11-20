Arr=[15,13,9,2]
def buble_sort(arr):
    N=len(arr)
    for i in range(N):
        for j in range(N-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)


def insert_sort(arr):
    N = len(arr)
    for i in range(N):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = tmp
    return arr

def insert_sort(arr):
    N = len(arr)
    for i in range(N):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = tmp
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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

        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    return C

def merge_sort(arr):
    N = len(arr)
    if N == 1:
        return arr

    ind = N//2
    L = arr[0:ind]
    R = arr[ind:]
    return merge(merge_sort(L), merge_sort(R))
print(merge_sort(Arr))


func=lambda x: x**2
print(func(2))
func2=lambda x,y:print(x**2+y**2)
func2(1,1)
