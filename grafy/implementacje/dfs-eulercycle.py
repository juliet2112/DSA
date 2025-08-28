def dfs(G):
    def dfs_visit(v):
        return
    
    for v in range (len(G)):
        for u in G[v]:
            dfs_visit(u)
