# Mamy graf G - nieskierowany
# Trzeba stwierdzieć czy G ma cykl składający się z 4 wierzchołków.

def dfs(G,k):
    def dfsvisit(G,v):
        nonlocal time
        visited[v] = True
        times[v] = time
        time+=1
        for u in G[v]:
            if visited[u] == False:
                return dfsvisit(G,u)

            elif(times[v] - times[u] == k-1):
                return True
        
        time -= 1 
        return False
    
    time = 0
    visited = [False for i in range(len(G))]
    times = [None for i in range (len(G))]

    for v in range (len(G)):
        if visited[v] == False and dfsvisit(G,v):
            return True
        
    return False

#G = [[1,2],[0,2,3,5],[0,1,4,6],[1,5,6],[2,5,8],[1,3,5],[2,3,7],[6,8],[4,7]]
G = [[1,2],[0,2,3],[0,1,3],[1,2,4],[3,5,6,7],[4],[4],[4,8],[7]]
print(dfs(G,3))
        