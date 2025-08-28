from zad8testy import runtests
from math import inf

def partition(p,r,T):
    x = (p+r)//2
    T[x],T[r] = T[r],T[x]
    i = p-1
    for j in range (p, r):
        if T[j] > T[r]:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[r] = T[r],T[i+1]
    return i+1

def quickselect(p,r,T):
    cur_min = inf
    while p <= r:
        q = partition(p,r,T)
        if(T[q] - q == 0):
            return T[q]
        elif q -T[q] > 0:
            r = q-1
            if (q-T[q]) <= cur_min:
                cur_min = q-T[q]
                mini = T[q]
        else:
            p = q+1
    return mini
   
    
def ice_cream( T ):
    n = len(T)
    maxi = quickselect(0,n-1,T)
    melted = 0
    suma = 0
    for i in range (n):
        if T[i] > maxi:
            suma += (T[i]-melted)
            melted +=1
    return suma





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
