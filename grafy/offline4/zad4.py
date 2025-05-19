from zad4testy import runtests
from math import inf
from queue import PriorityQueue

def make_graph(n, E, S):
    G = [[] for _ in range(n)]
    odd = [False for _ in range(n)]

    for i in S:
        odd[i] = True

    mem = S[0]

    for u,v,w in E:
        if odd[u] == True:
            if odd[v] == False:
                G[mem].append((v,w))
                G[v].append((mem,w))
        elif odd[v] == True:
            G[mem].append((u,w))
            G[u].append((mem,w))
        else:
            G[v].append((u,w))
            G[u].append((v,w))

    return G,odd

def dijkstra(a, b, G, n):
    d = [inf for _ in range (n)]

    PQ = PriorityQueue()
    d[a] = 0
    PQ.put((d[a],a))

    while not PQ.empty():
        dist,v = PQ.get()
        if v == b:
            return d[v]
        
        for u,w in G[v]:
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                PQ.put((d[u],u))
    
    return None


def spacetravel( n, E, S, a, b ):
    G,odd = make_graph(n,E,S)
    if odd[a] == True:
        a = S[0]
    if odd[b] == True:
        b = S[0]
    return dijkstra(a,b,G,n)

runtests( spacetravel, all_tests = True)
