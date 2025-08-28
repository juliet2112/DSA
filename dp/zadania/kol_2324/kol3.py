from kol3testy import runtests
from math import inf

def orchard(T, m):
    n = len(T)
    wyniki = [0 for _ in range (m)]
    prev = [0 for _ in range (m)]
    for i in range (n):
        for j in range (0, m):
            if (prev[j] != 0 or j == 0):
                wyniki[(j+T[i])%m] = max(prev[j]+1,prev[(j+T[i])%m])
        prev = wyniki[:]
    return n-wyniki[0]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)


"""def orchard(T, m):
    memo ={}
    def f(T,i,j,k):
        nonlocal memo
        if (i,j,k) in memo:
            return memo[(i,j,k)]
    
        if i == -1:
            return j==0 and k==0
    
        if j == 0:
            return i+1 == k
    
        if k < 0:
            return False
    
        if j < 0:
            return False
       
        wynik = f(T,i-1,j,k-1) or f(T,i-1,j-T[i],k)
        memo[(i,j,k)] = wynik
        return wynik
    
    n = len(T)
    suma = sum(T[0:n+1])
    for i in range (0,n):
        curr = m
        while curr < suma:
            if f(T,n-1,curr,i):
                return i
            curr+=m

    return n"""


"""def orchard(T, m):
    n = len(T)
    k = sum(T[0:n+1])
    wyniki = [[0,0] for _ in range (k)]
    curr_max = 0
    for i in range (n):
        for j in range (k):
            if i%2 == 1:
                if (wyniki[j][0] != 0 or j == 0) and j+T[i] < k:
                    wyniki[j+T[i]][1] = max(wyniki[j][0]+1,wyniki[j+T[i]][0])
                    if (j+T[i])%m == 0:
                        curr_max = max(wyniki[j+T[i]][1],curr_max)
                    wyniki[j][0] = max(wyniki[j][0], wyniki[j][1])
            else:
                if (wyniki[j][1] != 0 or j == 0) and j+T[i] < k:
                    wyniki[j+T[i]][0] = max(wyniki[j][1]+1,wyniki[j+T[i]][1])
                    if (j+T[i])%m == 0:
                        curr_max = max(wyniki[j+T[i]][0],curr_max)
                    wyniki[j][0] = max(wyniki[j][0], wyniki[j][1])


    return n-curr_max"""


"""def orchard(T, m):
    n = len(T)
    k = sum(T)
    wyniki = [0 for _ in range (k)]
    curr_max = 0
    for i in range (n):
        for j in range (k-1,-1,-1):
            if (wyniki[j] != 0 or j == 0) and j+T[i] < k:
                wyniki[j+T[i]] = max(wyniki[j]+1,wyniki[j+T[i]])
                if (j+T[i])%m == 0:
                    curr_max = max(wyniki[j+T[i]],curr_max)

    return n-curr_max"""