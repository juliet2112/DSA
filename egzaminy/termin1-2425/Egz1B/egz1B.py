#O(V^2 + EV), pamięć O(V^2)
#Wriant z dynamicznym liczeniem możliwych ścieżek, z u do v, gdy jest jedna taka możliwość, to jest to krawędź krytyczna
#Takie rozwiązanie wymaga sortowania topologicznego i przechodzenia "od korzenia do liści" zliczając możliwości
from egz1Btesty import runtests

def dfs(G):
    def dfsvisit(v):
        visited[v] = True
        for u in G[v]:
            if visited[u] == False:
                dfsvisit(u)
        sortedd.append(v)
        

    n = len(G)
    sortedd = []
    visited = [False for _ in range (n)]
    for v in range (n):
        if not visited[v]:
            dfsvisit(v)

    return sortedd

def create_graph(E,v):
    NG = [[] for _ in range (v)]
    for v,u in E:
        NG[v].append(u)

    return NG

def reverse(T):
    New_T = []
    while T:
        x = T.pop()
        New_T.append(x)

    return New_T

def critical(V, E):
    G = create_graph(E, V)
    topo = dfs(G)
    topo = reverse(topo)
    n = len(G)

    dp = [[0 for _ in range(n)] for _ in range (n)]
    for i in range (n):
        dp[i][i] = 1

    for a in range (n):
        for v in topo:
            for u in G[v]:
                dp[a][u] += dp[a][v]

    ile = 0
    for i,j in E:
        if dp[i][j] == 1:
            ile +=1

    return ile

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)

