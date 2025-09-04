#O(nE)
#f(i,b) - minimalny koszt znalezienia się na planecie i mając b ton paliwa
#sprawdzamy tylko możliwość dotarcia na planetę i z planety i-1, mamy dwie możliwości
#f(i,b) = min(lecimy bez zapasu paliwa i tankujemy do b na mniejscu, robimy niezbędny zapas paliwa na planecie i-1)
from egz1btesty import runtests
from math import inf

def planets( D, C, T, E ):
    n = len(D)
    f = [[inf for _ in range (E+1)] for _ in range(n)] 
    #min koszt znalezienia się na planecie i z paliwem 
    for i in range (n):
        for j in range (E+1):
            if i == 0:
                f[i][j] = j*C[i]
            else:
                mini = inf
                if D[i]-D[i-1]+j < E+1:
                    mini = min(mini,f[i-1][D[i]-D[i-1]+j])
                if j > 0:
                    mini = min(mini, f[i][j-1]+C[i])
                f[i][j] = min(mini,f[i][j])
        f[T[i][0]][0] = min(f[i][0]+T[i][1],f[T[i][0]][0])

    return f[n-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True)