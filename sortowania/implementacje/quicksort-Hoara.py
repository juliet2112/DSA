#optymalny pivot to mediana

def partition(T,l,r):
    i = l-1
    j = r
    pi = T[(l+r)//2]
    while True:

        i+=1
        while T[i] < pi:
            i+=1

        j-=1
        while T[j] > pi:
            j-=1

        if i >= j:
            return j
        
        T[i],T[j]=T[j],T[i]

def quicksort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        p=q+1

T = [23,46,2,43,1,12,78,24]
quicksort(T,0,len(T)-1)
for i in range (len(T)):
    print(T[i])