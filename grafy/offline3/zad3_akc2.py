from zad3testy import runtests
from collections import deque
from math import inf

def na_macierz(G):
    macierz = [[0 for i in range (len(G))] for i in range (len(G))]
    for i in range (len(G)):
        for j in range (len(G[i])):
            macierz[i][G[i][j]] = 1
    return macierz

def longer( G, s, t ):
    def bfs(G,s,t):
        Q = deque()
        visited = [False for i in range (len(G))]
        d = [inf for i in range (len(G))]
        Q.append(s)
        visited[s]=True
        d[s] = 0
        while (Q):
            v = Q.popleft()
            for u in range (len(G)):
                if G[v][u] == 1:
                    if visited[u] == False:
                        Q.append(u)
                        visited[u] = True
                        d[u] = d[v]+1
                        parent[u] = v
        return (d[t])
    
    parent = [None for i in range (len(G))]
    G = na_macierz(G)
    d = bfs(G,s,t)
    p = parent[t]
    k = t
    while k != s:
        G[p][k] = 0
        dnew = bfs(G,s,t)
        if (dnew > d): return (p,k)
        G[p][k] = 1
        k = p
        p = parent[p]
    
    return (None)

runtests( longer, all_tests = True)
