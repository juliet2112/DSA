from egzP1btesty import runtests 
from math import inf
from heapq import heappop, heappush
def create_graph(G):
    n = 0
    for u,v,d in G:
        n = max(n,v,u)

    New_G = [[] for _ in range (n+1)]
    for u,v,d in G:
        New_G[u].append((v,d))
        New_G[v].append((u,d))

    return New_G

def shortest(G,s,t):
    Q = [(0,s,0)]
    best = {}

    while Q:
        dist, v, n = heappop(Q)

        if n > 4:
            continue

        if (v, n) in best and best[(v, n)] < dist:
            continue

        best[(v,n)] = dist

        if n == 4 and v == t:
            return dist
        
        for u, w in G[v]:
            heappush(Q,(dist+w,u,n+1))



def turysta( G, D, L ):
    G = create_graph(G)
    return shortest(G,D,L)

runtests ( turysta )