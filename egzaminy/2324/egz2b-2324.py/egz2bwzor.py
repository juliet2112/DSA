#O(m) > O(2E) > O(E + V)
#BFS z throttlingiem: z oznaczaniem stanów: tego po jakim torze aktualnie jedzie pociąg
from egz2btesty import runtests
from math import inf
from collections import deque

def switch(s1,s2):
    if s1 == 2:
        return 0
    if s1 == 1 and s2 == 1: return 10
    if s1 == 0 and s2 == 0: return 5
    return 20

def bfs(G,s,t):
    n = len(G)
    Q = deque()
    visited = [False for _ in range (n)]
    d = [[inf for _ in range (n)] for _ in range (3)]
    d[2][s] = 0
    visited[s] = True
    Q.append((0,s,2))

    while Q:
        x,u,s1 = Q.popleft()
        if x != 0:
            Q.append((x-1,u,s1))
        else:
            for v, w, s2 in G[u]:
                way = w + switch(s1,s2)
                if d[s2][v] > way + d[s1][u]:
                    d[s2][v] = way + d[s1][u]
                    Q.append((way,v,s2))

    return min(d[0][t],d[1][t],d[2][t])

def create_graph(G):
    n = 0
    for u,v,d,s in G:
        n = max(n,v,u)

    New_G = [[] for _ in range (n+1)]
    for u,v,d,s in G:
        if s == 'I':
            New_G[u].append((v,d,0))
            New_G[v].append((u,d,0))
        else:
            New_G[u].append((v,d,1))
            New_G[v].append((u,d,1))

    return New_G

def tory_amos( E, A, B ):
  G = create_graph(E)
  d = bfs(G,A,B)
  return d

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )