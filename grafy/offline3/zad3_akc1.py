#Sprawdanie dla każdej krawędzi
#O(E^2 + EV)

from zad3testy import runtests
from collections import deque
from math import inf

def bfs(G,s,t,mem = (None,None)):
    Q = deque()
    visited = [False for i in range (len(G))]
    d = [inf for i in range (len(G))]
    Q.append(s)
    visited[s]=True
    d[s] = 0
    while (Q):
        v = Q.popleft()
        for u in G[v]:
            if((min(v,u),max(v,u)) != mem):
                if visited[u] == False:
                    Q.append(u)
                    visited[u] = True
                    d[u] = d[v]+1
    return (d[t])



def longer( G, s, t ):
    d = bfs(G,s,t)
    for i in range (len(G)):
        for j in range (len(G[i])):
            if( i < G[i][j]):
                mem = i,G[i][j]
                dnew = bfs (G,s,t,mem)
                if (dnew > d): return (mem)
    
    return (None)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )

