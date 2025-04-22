from math import inf
from queue import PriorityQueue

def dijkstra(s,G):
    visited = [False for i in range (len(G))]
    d = [inf for i in range (len(G))]
    parent = [None for i in range (len(G))]
    
    Q = PriorityQueue()
    d[s] = 0
    Q.put((d[s],s))

    while not Q.empty():
        (dist,v) = Q.get()
        if dist > d[v]:
            continue

        visited[v] = True
        for u,w in G[v]:
            if(d[v] + w < d[u]):
                d[u] = d[v] + w
                parent[u] = v
                Q.put((d[u], u))

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

d = dijkstra(0,G)
print(d[7])
