from zad1testy import runtests

def parent(x):
    return (x-1)//2

def heapify(A,n,i):
    l=2*i + 1
    r=2*i + 2
    max_ind = i
    if(l < n and A[l] > A[max_ind]):
        max_ind = l
    if(r < n and A[r] > A[max_ind]):
        max_ind = r
    if(max_ind != i):
        A[max_ind],A[i] = A[i],A[max_ind]
        heapify(A,n,max_ind)

def build_heap(A):
    n = len(A)
    for i in range (parent(n-1),-1,-1):
        heapify(A,n,i)
        

def heapsort(A):
    n = len(A)
    build_heap(A)
    for i in range (n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heapify(A,i,0)


def value(a):
    n=len(a)
    fleft=0
    fright=0
    mn=1
    for i in range (n):
        fleft += ord(a[i])*mn
        fright += ord(a[n-1-i])*mn
        mn*=23
    return (min(fleft,fright)%1000000007)

def strong_string(T):
    for i in range (len(T)):
        T[i]=value(T[i])
    heapsort(T)
    max=0
    curr=1
    for i in range (1,len(T)):
        if(T[i]==T[i-1]):
            curr+=1
        else:
            if(curr > max):
                max = curr
            curr = 1
    if(curr > max):
        max = curr

    return max


# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( strong_string, all_tests=False )
