#O(n^2)
#dynamicznie: f(i,j,dir) - maksymalna liczba komnat odwiedzonych w drodze do (i,j), przychodząc z określonego przez dir kierunku, tak aby nie powtarzać komnat
from egz3btesty import runtests
from math import inf
def maze( L ):
    n = len(L)
    memo = {}
    def dp (i,j,dir):
        if (i,j,dir) in memo:
            return memo [(i,j,dir)]
        
        elif i >= n or j < 0 or i < 0:
            wynik = -inf
        
        elif L[i][j] == '#':
            return -inf
        
        elif i == 0 and j == 0:
            wynik = 0
        
        elif dir == 'Up':
            wynik = max(dp(i+1,j,'Up')+1,dp(i,j-1,'Up')+1,dp(i,j-1,'Dw')+1)
        elif dir == 'Dw':
            wynik = max(dp(i-1,j,'Dw')+1,dp(i,j-1,'Up')+1,dp(i,j-1,'Dw')+1)


        memo[(i,j,dir)] = wynik
        return wynik
    
    return max(dp(n-1,n-1,'Up'),dp(n-1,n-1,'Dw'))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True)