from zad2testy import runtests
def merge(A,p,mid,r):
    inv = 0
    left_n = mid - p + 1
    right_n = r - mid 
    left = A[p:p+left_n]
    right = A[mid+1:mid+1+right_n]

    i,j = 0,0
    k = p
    while i < left_n and j < right_n:
        if left[i] <= right[j]:
            A[k]=left[i]
            i+=1
        else:
            A[k]=right[j]
            j+=1
            inv += left_n - i
        k+=1

    while i < left_n:
        A[k]=left[i]
        i+=1
        k+=1

    while j < right_n:
        A[k]=right[j]
        j+=1
        k+=1

    return inv
        


def mergesort(A,p,r):
    inv = 0
    if p < r:
        mid = (p+r)//2
        inv += mergesort(A,p,mid) + mergesort(A,mid+1,r) + merge(A,p,mid,r)
    return inv

def count_inversions(A):
    return mergesort(A,0,len(A)-1)



# Zakomentuj gdy uruchamiasz duze testy
runtests( count_inversions, all_tests=True )
