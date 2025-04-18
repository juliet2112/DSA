from kol1testy import runtests

def partition(A, p, r):
    x = (p + r) // 2
    A[r], A[x] = A[x], A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] > A[r]:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickselect(A, p, r, k):
    while p < r:
        q = partition(A, p, r)
        if q == k:
            return A[k]
        elif k < q:
            r = q - 1
        else:
            p = q + 1
    return A[k]

def ksum(T,k,p):
    n = len(T)
    suma = 0
    for i in range (n-p+1):
        A = T[i:i+p]
        suma+=quickselect(A,0,p-1,k-1)
    return suma

runtests( ksum, all_tests=True)