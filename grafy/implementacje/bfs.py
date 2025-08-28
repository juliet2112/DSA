from collections import deque
from math import inf

def bfs(G,s):
    Q = deque()
    visited = [False for i in range(len(G))]
    parent = [None for i in range (len(G))]
    d = [inf for i in range (len(G))]

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while Q:
        v = Q.popleft()
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                parent[u] = v
                d[u] = d[v]+1
                Q.append(u)

    print(d[8])

G = [[1,2],[0,2,3,5],[0,1,4,6],[1,5,6],[2,5,8],[1,3,5],[2,3,7],[6,8],[4,7]]
bfs(G,0)
