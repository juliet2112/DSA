#O(nm)
#f(i,j) = minimalna suma odległości biurowców z pozycji X[0],...,X[i] do przydzielonych im działek, przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y [j].
#w cur_min przechowuję minimalną wartość połączenia i biurowców, do j parkingów bez warunku, że i-ty musi być przypisany do j-tego
#pozwala to uniknąć szukania minimalnej wartości i poprawia złożoność
from egz2btesty import runtests
from math import inf

def parking(X,Y):
    m = len(Y)
    n = len(X)
    def d(i,j):
        return abs(X[i]-Y[j])

    dp = [[inf for _ in range (m)] for _ in range (n)]

    for i in range (m):
        dp[0][i] = d(0,i)

    for i in range (1,n):
        cur_min = inf
        for j in range (i,m):
            cur_min = min(cur_min, dp[i-1][j-1])
            dp[i][j] = cur_min + d(i,j)

    return min(dp[n-1])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True)