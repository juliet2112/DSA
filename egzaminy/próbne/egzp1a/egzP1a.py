#O(n)
#Dynamicznie mini(i) = minimalna liczba liter z jakich można ułożyć napis do i-tego znaku
#Każda litera składa się z maksymalnie 4 znaków, więc dla każdego znaku sprawdzamy cztery zaczynające się od niego prefixy i jeżeli mamy dostępny taki znak to aktualizujemy mini
from egzP1atesty import runtests 
from math import inf
def tomorse(W,memo):
    word = ''
    for a in W:
        word+=memo[a]
    return word

def todict(M):
    memo = {}
    for a,b in M:
        memo[a] = b
    return memo

def titanic( W, M, D ):
    memo = todict(M)
    W = tomorse(W,memo)
    n = len(W)
    znaki = set()
    for a in D:
        z = M[a]
        znaki.add(M[a][1])

    mini = [inf for _ in range (n+1)]
    mini[0]= 0

    for i in range (1,n+1):
        for j in range (0,4):
            if i+j > n:
                continue
            if W[i-1:i+j] in znaki:
                mini[i+j] = min(mini[i+j],mini[i-1]+1)

    return mini[n]

runtests ( titanic, recursion=False )