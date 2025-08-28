
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
        p=q+1

T = [3,4,2,56,12,25,1,2]
quicksort(T,0,7)
for i in range (len(T)):
    print(T[i])