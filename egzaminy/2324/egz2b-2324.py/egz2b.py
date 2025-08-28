from egz2btesty import runtests
from math import inf
from heapq import heappop, heappush

def switch(s1,s2):
    if s1 == 1 and s2 == 1: return 5
    if s1 == 0 and s2 == 0: return 10
    return 20

def dijkstra(G,s,t):
    n = len(G)
    d = [[inf for _ in range (n)] for _ in range (2)]
    #0 - 'I', 1 - 'P'
    PQ = []
    d[0][s] = 0
    d[1][s] = 0
    for u, w, s2 in G[s]:
        d[s2][u] = w  
        heappush(PQ,(w,u,s2))

    while PQ:
        dist, v,s1 = heappop(PQ)
        if dist > d[s1][v]: continue

        for u,w,s2 in G[v]:
            way = w + d[s1][v] + switch(s1,s2)
            if d[s2][u] > way:
                d[s2][u] = way
                heappush(PQ,(d[s2][u],u,s2))

    return min(d[0][t], d[1][t])

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
  d = dijkstra(G,A,B)
  return d

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )