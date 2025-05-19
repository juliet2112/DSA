# szukam odległości z wierzchołka startowego do każdego z resortów
# oznaczam wierzchołki z resortami jako takie, przez które nie można przejść, jedynie do nich dotrzeć (ozn. -1)
# gdyż jeśli istniałaby trasa z s do resortu B, przez resort A, to trasa do resortu A będzie krótsza, więc wybiorę zawsze A
# późniejsze pokonanie tej trasy nie będzie możliwe
# O(E + ElogV + VlogV)= O(ElogV)

from kol2testy import runtests
from queue import PriorityQueue
from math import inf

def dijkstra(G,s,visited):
    d = [inf for _ in range(len(G))]
    Q = PriorityQueue()
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        dist, v = Q.get()
        if dist > d[v]:
            continue
        if visited[v] == 1 or visited[v] == -1:
            continue
        for u, w in G[v]:
            if visited[u] == 1:
                continue
            if d[v] + w < d[u]:
                d[u] = d[v] + w
                Q.put((d[u], u))
        visited[v] = 1

    return d

def ile_w(E):
    n = 0
    for u,v,w in E:
        n = max(n,u,v)
    return n

def create_graph(E):
    n = ile_w(E)
    A = [[] for _ in range (n+1)]
    for u,v,w in E:
        A[u].append((v,w))
        A[v].append((u,w))
    return A

def lets_roll(start_city, flights, resorts):
    G = create_graph(flights)
    suma = 0
    visited = [0 for _ in range(len(G))]
    for i in resorts:
        visited[i] = -1

    d = dijkstra(G, start_city,visited)
    for i in resorts:
        if d[i] != inf:
            suma += d[i]*2
       
    return suma

runtests(lets_roll, all_tests = True)
