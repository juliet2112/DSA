from zad3testy import runtests
from collections import deque
from math import inf

def bfs(G,s,t):
    Q = deque()
    visited = [False for i in range (len(G))]
    d = [inf for i in range (len(G))]
    Q.append(s)
    visited[s]=True
    d[s] = 0
    while (Q):
        v = Q.popleft()
        for u in G[v]:
            if visited[u] == False:
                Q.append(u)
                visited[u] = True
                d[u] = d[v]+1
    return (d[t])



def longer( G, s, t ):
    d = bfs(G,s,t)
    for i in range (len(G)):
        for j in range (len(G[i])):
            mem = G[i][j]
            G[i][j] = i
            dnew = bfs (G,s,t)
            if (dnew > d): return (i,mem)
            G[i][j] = mem
    
    return (None)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
