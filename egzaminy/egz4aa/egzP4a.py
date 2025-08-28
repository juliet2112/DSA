from egzP4atesty import runtests 
#O(nlogn)
def binary_search(A, k):
    n = len(A)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            return mid
        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return left

def mosty ( T ):
    T.sort(key=lambda x: x[0])
    V = [v for _, v in T]
    naj = []

    for v in V:
        i = binary_search(naj,v)
        if i == len(naj):
            naj.append(v)
        else:
            naj[i] = v

    return len(naj)

runtests ( mosty, all_tests=True)

"""
O(n^2)
def mosty ( T ):
    T.sort(key=lambda x: x[0])
    n = len(T)
    F = [1 for _ in range(n)]
    maxi = 0
    for i in range (1,n):
        for j in range (i):
            if T[j][1] < T[i][1] and F[j]+1 > F[i]:
                F[i] = F[j]+1
        if F[i] > F[maxi]: maxi = i
    return F[maxi]"""