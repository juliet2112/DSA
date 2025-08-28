from zad7testy import runtests

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
