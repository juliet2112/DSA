from math import inf
from heapq import heappop, heappush

def dijkstra(G,s):
    n = len(G)
    d = [inf for _ in range (n)]
    PQ = []
    d[s] = 0
    heappush(PQ,(d[s],s))

    while PQ:
        dist, v = heappop(PQ)
        if dist > d[v]: continue

        for u,w in G[v]:
            if d[u] > w + d[v]:
                d[u] = w + d[v]
                heappush(PQ,(d[u],u))

    return d


G = [
    [(1, 3), (6, 2)],
    [(0, 3), (2, 2), (8, 1)],
    [(1, 2), (3, 5)],
    [(4, 20), (2, 5), (8, 1)],
    [(5, 8), (3, 20), (7, 2)],
    [(6, 3), (7, 1), (4, 8)],
    [(0, 2), (7, 1), (5, 3)],
    [(6, 1), (5, 1), (8, 7), (4, 2)],
    [(7, 7), (1, 1), (3, 1)]
]

d = dijkstra(G,0)
print(d[7])