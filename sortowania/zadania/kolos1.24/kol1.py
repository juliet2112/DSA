#tworzę tablicę struktur zawerających element tablicy i jego początkowy indeks 
#sortuję elementy rosnąco po wartości używając quicksorta
#dla każdego elementu liczę różnicę indeksu początkowego i po posortowaniu, szukam maximum po tej wartości
#nie dla każdej liczby będzie to ale dla ostatniej tak, bo zaburzyć by to mogła tylko większa liczba znajdująca się za nią, a to dawałoby nowe maximum
#złożoność czasowa: O(2n + nlogn) = O(nlogn) , pamięciowa O(n) (chyba)

from kol1testy import runtests
class element:
    def __init__(self,val,pos):
        self.val = val
        self.pos = pos
        

def partition(A,p,r):
    x = (p+r)//2
    A[x],A[r]=A[r],A[x]
    i = p-1
    for j in range(p,r):
        if(A[j].val>=A[r].val):
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r]=A[r],A[i+1]
    return(i+1)

def quicksort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        p = q+1

def maxrank(T):
    for i in range (len(T)):
        T[i] = element(T[i],i)
    quicksort(T,0,len(T)-1)
    max_r = 0
    for i in range (len(T)):
        if(T[i].pos - i > max_r): max_r = T[i].pos - i
    return(max_r)

#T = [12,17,6,7,16,13,10,19,12,17]
#print(maxrank(T))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests = True)