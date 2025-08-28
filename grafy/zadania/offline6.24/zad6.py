from zad6testy import runtests
from math import inf
from heapq import heappop, heappush

def dijkstra(G,s,w):
    n = len(G)
    d = [[inf]*2 for _ in range(n)]
    state = 0
    d[s][0] = 0
    d[s][1] = 0
    PQ = [(0,s,state)]

    while len(PQ) != 0:
        dist, v, state = heappop(PQ)
        if dist > d[v][state]:
            continue

        if v == w:
             return min(d[v][0],d[v][1])

        for u in range (n):
            w1 = G[v][u]
            if w1 == 0:
                 continue
            if d[v][state] + w1 < d[u][0]:
                    d[u][0] = d[v][state] + w1
                    heappush(PQ,(d[u][0],u,0))
            if state == 0:
                for z in range(n):
                     if G[u][z] == 0 or z == v:
                        continue
                     w2 = max(w1, G[u][z])
                     if d[z][1] > d[v][state] + w2:
                          d[z][1] = d[v][state] + w2
                          heappush(PQ,(d[z][1],z,1))

    return min(d[w][0],d[w][1])
    


def jumper( G, s, w ):
    
    return dijkstra(G,s,w)

runtests( jumper, all_tests = True )