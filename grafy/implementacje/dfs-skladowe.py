def dfs(G):
    def dfsvisit(G,v):
        visited[v] = True
        for u in G[v]:
            if visited[u] == False:
                dfsvisit(G,u)

    visited = [False for i in range (len(G))]
    skladowe = 0
    for v in range (len(G)):
        if visited[v] == False:
            skladowe+=1
            dfsvisit(G,v)
    
    return skladowe


G = [[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[0,2,4],[]]
print(dfs(G))
