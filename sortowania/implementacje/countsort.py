def countsort(A,k):
    n = len(A)
    C = [0]*k
    B = [0]*n
    for i in range (n):
        C[A[i]]+=1

    for i in range (1,k):
        C[i]+=C[i-1]

    for i in range(n-1,-1,-1):
        C[A[i]]-=1
        B[C[A[i]]] = A[i]

    for i in range (n):
        A[i] = B[i]

A = [5,4,0,2,1,3,2,3,2]
countsort(A,6)
for i in range (len(A)):
    print(A[i])