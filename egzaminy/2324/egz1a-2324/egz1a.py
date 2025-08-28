from egz1atesty import runtests

from queue import PriorityQueue
from math import inf

def dijkstra(s, G):
    d = [inf for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    Q = PriorityQueue()
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        dist, v = Q.get()
        if dist > d[v]:
            continue
        if visited[v]:
            continue
        for u, w in G[v]:
            if d[v] + w < d[u]:
                d[u] = d[v] + w
                Q.put((d[u], u))
        visited[v] = True

    return d

def create_graph(G):
    n = 0
    for u,v,d in G:
        n = max(n,v,u)

    New_G = [[] for _ in range (n+1)]
    for u,v,d in G:
        New_G[u].append((v,d))
        New_G[v].append((u,d))

    return New_G


def armstrong( B, G, s, t):
    G = create_graph(G)
    D = dijkstra(s,G)
    D2 = dijkstra(t,G)
    mini = D[t]

    for i,p,q in B:
        mini = min(mini, D2[i]*(p/q)+D[i])

    return int(mini)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True)