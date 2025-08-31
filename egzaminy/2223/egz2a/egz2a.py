#O(n^2)
from egz2atesty import runtests
def dominance(P):
    n = len(P)
    dom = [0 for _ in range (n)]
    for i in range(n):
        for j in range(i+1,n):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                dom[i]+=1
            if P[j][0] > P[i][0] and P[j][1] > P[i][1]:
                dom[j]+=1
    return max(dom)
        

    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True)
