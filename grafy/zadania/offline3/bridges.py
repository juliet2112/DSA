def bridges(G):
    n = len(G)
    time = 0

    parents = [None] * n
    d = [float('inf')] * n
    low = [float('inf')] * n
    bridges = []
    aps = []

    def DFSVisit(G, u):
        nonlocal time

        children = 0

        d[u] = time
        low[u] = time
        
        time += 1

        for v in G[u]:
            if d[v] == float('inf'):
                parents[v] = u
                children += 1
                low[u] = min(low[u], DFSVisit(G, v)) #dfs == low(w)

                if parents[u] is None and children > 1:
                    aps.append(u)

                elif parents[u] is not None and low[v] >= d[u]:
                    aps.append(u)

            elif v != parents[u]: # aby nie wrócić do parenta
                low[u] = min(low[u], d[v]) # check krawędzi wstecznych

        if low[u] == d[u] and parents[u] != None:
            bridges.append((u, parents[u]))

        return low[u]


    for u in range(n): # jeżeli na pewno spójny to można bez tego
        if d[u] == float('inf'):
            DFSVisit(G, u)

    return bridges, aps

#G = [[3, 9],[2, 3],[1, 3, 4],[0, 1, 2],[2, 5, 6, 8],[4, 6],[4, 5, 7],[6, 8],[4, 7],[0]]

G = [[1,2],[0,3],[0,4],[1,5,6],[2,7],[3,8],[3,8],[4,8],[5,6,7,9],[8,10,11],[9,12],[9,12],[10,11]]

#G = [[1,2],[0,2],[0,1,3,4],[2,5],[2,4],[3,4]]

print(bridges(G))