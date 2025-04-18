def dfs(G):
    def dfsvisit(G,v):
        visited[v] = True
        for u in G[v]:
            if visited[u] == False:
                dfsvisit(u)

    visited = [False for i in range (len(G))]
    for v in range (len(G)):
        if visited[v] == False:
            dfsvisit(G,v)

    
