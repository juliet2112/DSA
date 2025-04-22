from math import inf
from queue import PriorityQueue

def relax(u,v,d,parent):
    if(d[v] + u[1] < d[u[0]]):
        d[u[0]] = d[v] + u[1]
        parent[u[0]] = v

def dijkstra(s,G):
    visited = [False for i in range (len(G))]
    d = [inf for i in range (len(G))]
    parent = [None for i in range (len(G))]
    Q = PriorityQueue()
    d[s] = 0
    Q.put((d[s],s))
    while not Q.empty():
        (dist,v) = Q.get()
        visited[v] = True
        for u in G[v]:
            if visited[u[0]] == False:
                relax(u,v,d,parent)
                Q.put((d[u[0]], u[0]))

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