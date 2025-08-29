#O(VE) <= O(V(V+E)) bo V^2 <= VE
#Dla każdego grzyba wykonuję bfs obliczający odległość wszystkich wierzchołków od niego
#Czyli w pesymistycznym przypadku V razy
#Porównuję odległości i ustalam opanowanie przez grzyb d
from egz3atesty import runtests
from collections import deque
from math import inf

def bfs(G,s):
    n = len(G)
    Q = deque()
    d = [inf for _ in range(n)]
    d[s] = 0
    Q.append(s)

    while Q:
       v = Q.pop()
       for u in G[v]:
            if d[v]+1 < d[u]:
                d[u] = d[v]+1
                Q.append(u)
    return d

  
def mykoryza(G,T,d):
    n = len(G)
    typ = [[inf,None]for _ in range (n)]
    for v in T:
        dist = bfs(G,v)
        for i in range (n):
            if typ[i][0] > dist[i]:
                typ[i][0] = dist[i]
                typ[i][1] = v
    cnt = 0
    g = T[d]
    for i in range (n):
        if typ[i][1] == g:
            cnt+=1

    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True)