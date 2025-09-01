from egzP5btesty import runtests 
from math import inf
def create_graph(B):
    n = 0
    sett = set()
    for a, b in B:
        if (a,b) not in sett and (b,a) not in sett:
            sett.add((a,b))
        if max(a,b) > n:
            n = max(a,b)

    G = [[]for _ in range(n+1)]
    for v,u in sett:
            G[v].append(u)
            G[u].append(v)

    return G

def dfs(G):
    def dfsvisit(G,v):
        nonlocal time
        child = 0
        time +=1
        d[v] = time
        low[v] = time
        for u in G[v]:
            if d[u] == inf:
                parent[u] = v
                low[v] = min(dfsvisit(G,u),low[v])
                child +=1

                if parent[v] is not None and low[u] >= d[v]:
                    aps.add(v)

                if parent[v] is None and child> 1:
                    aps.add(v)

            elif u != parent[v]:
                low[v] = min(low[v], d[u])

        return low[v]


    time = 0
    aps = set()
    d = [inf for _ in range (len(G))]
    parent = [None for _ in range (len(G))]
    low = [inf for _ in range(len(G))]

    for s in range(len(G)):
        if d[s] == inf:
            dfsvisit(G,s)
    return len(aps)

def koleje ( B ):
    G = create_graph(B)
    wynik = dfs(G)
    return wynik
    

runtests ( koleje, all_tests=True)