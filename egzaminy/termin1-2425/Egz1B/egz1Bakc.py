#Dla każdej krawędzi grafu (v,u), sprawdzam, czy jej usunięcie spowoduje brak połączenia miedzy wierzchołkami v i u
# O(EV + E^2) 
from egz1Btesty import runtests

def dfs(G, s, k):
    def dfsvisit(G, v):
        nonlocal s
        nonlocal k
        visited[v] = True
        for u in G[v]:
            if v == s and u == k:
                continue
            if not visited[u]:
                dfsvisit(G, u)

    visited = [False for _ in range(len(G))]
    dfsvisit(G, s)
    return visited[k]

def create_graph(E,v):
    NG = [[] for _ in range (v)]
    for v,u in E:
        NG[v].append(u)

    return NG

def critical(V, E):
    ile = 0
    G = create_graph(E,V)
    for v,u in E:
        if dfs(G,v,u) == False:
            ile+=1

    return ile
        
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)
