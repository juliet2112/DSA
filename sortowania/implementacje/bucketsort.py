def partition(A,p,r):
    x = (p+r)//2
    A[r],A[x] = A[x],A[r]
    i = p -1
    for j in range (p,r):
        if(A[j]<A[r]):
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


def quicksort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        p = q+1

def bucketsort(A,p,k):
    n = len(A)
    numb = n//2
    zak = (k-p)/numb
    Buckets = [[] for i in range(numb)]

    for i in range (n):
        Buckets[int(A[i]/zak)].append(A[i])

    for i in range (numb):
        quicksort(Buckets[i],0,len(Buckets[i])-1)

    k = 0
    for i in range (numb):
        for j in Buckets[i]:
            A[k]=j
            k+=1


A = [0.23, 0.85, 0.12, 0.67, 0.34, 0.91, 0.45, 0.78, 0.56, 0.19]
bucketsort(A,0,1)
for i in range (len(A)):
    print(A[i])