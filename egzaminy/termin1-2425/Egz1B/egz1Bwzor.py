#O(V^2 + VE), pamięć O(V^2)
#Wykonuję dfs dla każdego wierzchołka oznaczając te, do których da się z niego dotrzeć 
#Dla każdej krawędzi (u,v) sprawdzam istnienie alternatywnego połączenia - takiego wierzchołka, do którego da się dotrzeć z u, i z którego istnieje droga do v
from egz1Btesty import runtests

def dfs(G):
    def dfsvisit(v):
        visited[v] = True
        for u in G[v]:
            if visited[u] == False:
                dfsvisit(u)

    n = len(G)
    ways = [[False for _ in range(n)] for _ in range (n)]
    for v in range (n):
        visited = [False for _ in range (n)]
        dfsvisit(v)
        for u in range(n):
            ways[v][u] = visited[u]

    return ways

def create_graph(E,v):
    NG = [[] for _ in range (v)]
    for v,u in E:
        NG[v].append(u)

    return NG

def critical(V, E):
    G = create_graph(E,V)
    ways = dfs(G)
    ile = 0
    n = len(G)

    for a,b in E:
        critical = True
        for i in range (n):
            if i == b or i == a:
                continue
            if ways[a][i]:
                if ways[i][b]:
                    critical = False
                    break
        if critical:
            ile+=1

    return ile 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)
