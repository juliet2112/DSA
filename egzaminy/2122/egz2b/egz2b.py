#O(n)
#Dla każdego wierzchłka do którego da się wejść rozważam wszystkie trzy drogi, jeżeli prowadzą do wierzchołków
#Dla każdego z wierzchołków przechowuję maksymalne wartości
#Testy działają dla zał. że trzeba zostawić dokładnie tyle sztabek ile wynosi opłata za przejście, nie dowolną ilość
from egz2btesty import runtests
from math import inf
def magic( C ):
    n = len(C)
    dp = [-1 for _ in range (n)]
    dp[0] = 0
    for j in range (n-1):
        G = C[j][0]
        for k in range (1,4):
            x,y = C[j][k][0], C[j][k][1]
            if y != -1:
                tempa = G - x
                if tempa <= 10:
                    if dp[j] != -1 and dp[j] + tempa >= 0:
                        dp[y] = max(dp[j] + tempa, dp[y])

    return dp[n-1]

    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True)