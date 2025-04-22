from math import inf

def bellmanford(s,G):
    d = [inf for i in range (len(G))]
    parent = [None for i in range (len(G))]

    d[s] = 0

    for _ in range (len(G)-1):
        for v in range (len(G)):
            for u,w in G[v]:
                if d[u] > d[v] + w:
                    d[u] = d[v] + w
                    parent[u] = v

    for v in range(len(G)):
        for u,w in G[v]:
            if d[u] > d[v] + w:
                return None
            
    return d

G = [
    [(3,8),(2,5)], 
    [(0,1)], 
    [(3,6)], 
    [(1,10),(5,3)], 
    [(2,8)],
    [(4,-16)]
] 

d = bellmanford(0,G)
print(d[0])