#0(nk)
#dynamicznie : dp[k][n] - maksymalny podciąg z dokładnie k usuniętymi elementami kończący się na n
#dp[i][j] = max(dp[i][j-1] + T[j], dp[i-1][j-1])
#rozpatrujemy też moment kiedy bardziej opłaca się zacząc nowy podciąg od elementu x niż sumować do kolejnego - można to zrobić w dwóch przypadkach:
#kiedy nie usuwamy żadnego elementu i bieżemy sam x, lub usuwamy 1 element (czyli usuwamy x i wartość podciągu jest równa 0)

from egz1btesty import runtests
from math import inf
   
def kstrong(T, k):
    n = len(T)
    maxx = 0
    dp = [[0 for _ in range (n)] for _ in range (k+1)]
    dp[0][0] = T[0]
    for i in range (1,n):
        dp[0][i] = max(dp[0][i-1] + T[i], T[i])
    for i in range (1,k+1):
        for j in range (i,n):
            if i == 1:
                dp[i][j] = max(dp[i][j-1] + T[j], dp[i-1][j-1], 0)
            else:
                dp[i][j] = max(dp[i][j-1] + T[j], dp[i-1][j-1])
            maxx = max(dp[i][j],maxx)


    return maxx






# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )