#Julia Jamorska
#Tworzę tablicę rozmiaru 4*(m+n), następnie przypisuję do poszczególnych pozycji katapulty i procesy (coś w stylu count sorta),
#Idąc od tyłu dodaję na stos procesy do dopasowania do katpult i dla każdej z nich sprawdzam, czy istnieje proces w zasięgu, nie zajęty przez inną katapultę
#sprawdzam tylko najbliższe możliwe dopasowanie
#Złożoność: O(m+n)

from egz1Atesty import runtests

def make_table(P,K,R):
    n = len(K)
    m = len(P)
    New_T = [0 for _ in range (4*(n+m) +1)]
    for p in P:
        New_T[p] = -1

    for i in range (n):
        New_T[K[i]] = R[i]

    return New_T


def battle(P,K,R):
    T = make_table(P,K,R)
    ile = 0
    stack = []

    for i in range (len(T)-1,-1,-1):
        if T[i] == -1:
            stack.append(i)
        elif T[i] != 0 and len(stack) != 0:
            if stack[len(stack)-1] <= T[i]+i:
                ile+=1
                stack.pop()

    return ile
        
    
#zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True)

""" 
def lds(A):
    n = len(A)
    F = [1 for _ in range (n)]
    maxi = 0
    for i in range (1,n):
        for j in range (i):
            if A[j][1] > A[i][1] and F[j]+1 > F[i]:
                F[i] = F[j] + 1
        if F[i] > F[maxi]: maxi = i
    return F[maxi]



   n = len(K)
    m = len(P)
    ile = 0
    maxx = 0
    KR = [(K[i],R[i]) for i in range (n)]
    KR.sort(key=lambda x: x[0])
    PfK = []

    for k,r in KR:
        if k > maxx:
            if PfK:
                PfK.sort(key=lambda x: x[0])
                ile += lds(PfK)
                PfK = []

        maxx = max(maxx,k+r)
        for i in P:
            if i < k+r:
                PfK.append((i,k))


    if PfK:
        PfK.sort(key=lambda x: x[0])
        ile += lds(PfK)


    return ile"""

"""n = len(K)
    m = len(P)
    ile = 0
    KR = [(K[i],R[i]) for i in range(n)]
    for i in range (m):
        KR.append((P[i],0))

    KR.sort(key= lambda x: x[0])
    stack = []
    for i in range (n+m):
        if KR[i][1] != 0:
            stack.append(KR[i][1]+KR[i][0])
        else:
            while stack:
                kat = stack.pop()
                if (kat > KR[i][0]):
                    ile+=1
                    break
        
    return ile"""


"""def battle(P,K,R):
    n = len(K)
    m = len(P)
    l = max(max(K),max(P))
    KR = [0 for _ in range(l+1)]
    for i in range (m):
        KR[P[i]] = -1

    for i in range (n):
        KR[K[i]] = R[i]

    memo={}
    def f(KR,i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i >= j:
            return 0
        
        if j == i+1:
            if KR[i] > 0 and KR[j] == -1:
                return 1
            else:
                return 0
        
        result1 = 0
        for p in range (i+1,j-1):
            result1 = max(result1,f(KR,i,p)+f(KR,p+1,j))

        result2 = 0
        if KR[i] > j and KR[j] == -1:
            result2 = f(KR,i+1,j-1) + 1
        else:
            result2 = f(KR,i+1,j-1)

        return max(result1,result2)
    
    return f(KR,0,l)"""

"""def lds(A):
    n = len(A)
    F = [1 for _ in range (n)]
    maxi = 0
    for i in range (1,n):
        for j in range (i):
            if A[j] > A[i] and F[j]+1 > F[i]:
                F[i] = F[j] + 1
        if F[i] > F[maxi]: maxi = i
    return F[maxi]
"""
