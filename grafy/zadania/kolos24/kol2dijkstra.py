from kol2testy import runtests
from math import inf
from heapq import heappop, heappush
def ile_wierzcholow(G):
    maxi = G[0][0]
    for a,b,c in G:
        if a > maxi:
            maxi = a
        if b > maxi:
            maxi = b
    return maxi+1
          
def create_graph(G,n):
    NG = [[] for _ in range (n)]
    for v,u,w in G:
        NG[v].append((u,w))
        NG[u].append((v,w))
    return NG

def dijkstra(G,s,t,n):
    d = [[inf]*17 for _ in range (n)]

    d[s][0] = 0
    PQ = [(d[s][0],0,s)]

    while len(PQ)!= 0:
        dist,tired,v = heappop(PQ)

        if v == t:
            break

        if dist > d[v][tired]:
            continue

        for u,w in G[v]:
                new_tired = tired + w
                if new_tired> 16:
                    new_tired = w
                    w += 8

                way = w+d[v][tired]
                if way < d[u][new_tired]:
                    d[u][new_tired] = way
                    heappush(PQ,(way,new_tired,u))

    min = inf
    for i in range (17):
        if d[t][i] < min:
            min = d[t][i]

    return min

def warrior( G, s, t):
  
  n = ile_wierzcholow(G)
  create_graph(G,n)
  New_graph = create_graph(G,n)
  return dijkstra(New_graph,s,t,n)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests = True)