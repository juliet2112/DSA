#O(nlogn)
from egz1atesty import runtests

def snow( S ):
    n = len(S)
    S.sort(reverse=True)
    suma = 0
    for i in range (n):
        if S[i] - i > 0:
            suma += S[i]-i
    return suma
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )