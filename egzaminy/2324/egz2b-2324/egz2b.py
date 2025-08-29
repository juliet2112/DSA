#O(mlogm) > O(mlogn)
#Dijkstra z oznaczaniem stanów: tego po jakim torze aktualnie jedzie pociąg

from egz2btesty import runtests
from math import inf
from heapq import heappop, heappush

def switch(s1,s2):
    if s1 == 2:
        return 0
    if s1 == 1 and s2 == 1: return 10
    if s1 == 0 and s2 == 0: return 5
    return 20

def dijkstra(G,s,t):
    n = len(G)
    d = [[inf for _ in range (n)] for _ in range (3)]
    #0 - 'I', 1 - 'P', 2 - start
    PQ = []
    d[2][s] = 0
    heappush(PQ,(0,s,2))


    while PQ:
        dist, v,s1 = heappop(PQ)
        if dist > d[s1][v]: continue

        if v == t:
            return dist

        for u,w,s2 in G[v]:
            way = w + dist + switch(s1,s2)
            if d[s2][u] > way:
                d[s2][u] = way
                heappush(PQ,(d[s2][u],u,s2))

    return min(d[0][t], d[1][t], d[2][t])

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