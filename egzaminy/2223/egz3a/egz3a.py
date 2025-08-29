#O(n^2), a nawet O(nlogn)
#dijkstra z podziałem na stany, czyli po ilu godzinach rycerz dojechał do wierzchołka
#kiedy jest to niezbędne to dodaję 8h odpoczynku
from egz3atesty import runtests
from heapq import heappop, heappush
from math import inf
def add8(x,w):
    if x+w > 16:
        return [8, 0]
    return [0, x+w]

def dijkstra(G,s,t):
    n = len(G)
    d = [[inf for _ in range (17)] for _ in range (n)]
    Q = []
    d[s][0] = 0
    #dystans, wierzchołek, i kiedy ostatnio postój
    heappush(Q,(0,s,0))
    while Q:
        dist,v,curr = heappop(Q)
        if dist > d[v][curr]:
            continue
        for u,w in G[v]:
            stat = add8(curr,w)
            if d[u][stat[1]] > d[v][curr] + w + stat[0]:
                d[u][stat[1]] = d[v][curr] + w + stat[0]
                heappush(Q,(d[u][stat[1]],u,stat[1]))

    return min(d[t])

def create_graph(G):
    n = len(G)
    New_G = [[] for _ in range (n)]
    for i in range (n):
        for j in range (n):
            if G[i][j] != -1:
                New_G[i].append((j,G[i][j]))

    return New_G

def goodknight( G, s, t ):
    G = create_graph(G)
    ans = dijkstra(G,s,t)
    return ans
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True)