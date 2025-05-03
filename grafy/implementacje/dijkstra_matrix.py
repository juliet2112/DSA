from math import inf

def dijkstra_matrix(s,G):
    n = len(G)
    d = [inf for _ in range (n)]
    parent = [None for _ in range (n)]
    visited = [False for _ in range (n)]

    d[s] = 0


    while True:
        min_dist = inf
        min_index = -1
        for i in range (n):
            if d[i] < min_dist and visited[i] == False:
                min_dist = d[i]
                min_index = i
                
        if min_index == -1:
            return d
        
        visited[min_index] = True

        for v in range(len(G[min_index])):
            if d[v] > d[min_index] + G[min_index][v]:
                d[v] = d[min_index] + G[min_index][v]
                parent[v] = min_index

