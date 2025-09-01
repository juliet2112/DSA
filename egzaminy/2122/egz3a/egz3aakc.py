#O(n^2)
from egz3atesty import runtests
        
def snow( T, I ):
    A = [0 for _ in range (T)]
    for a,b in I:
        for j in range (a,b+1):
            A[j]+=1

    maxi = 0
    for i in range (T):
        maxi = max(maxi,A[i])

    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests = False )