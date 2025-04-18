from zad3testy import runtests
from collections import deque
from math import inf

#Za pomocą algorytmu bfs wyznaczam najkrótszą drogę z s do każdego z wierzchołków
#Sprawdzam jaka jest odległość sąsiadujących z t wierzchołków od s
#jeżeli d[t]= inf, to połączenie nie istnieje
#Rozpartuję trzy przypadki:
#t ma tylko jednego sąsiada: wtedy po usunięciu połączenia d[t] = inf
#tylko jeden z sąsiadów (i-ty) umożliwia dotarcie do t pokonując najkrótszą drogę (d[i] == d[t]-1), wtedy usuwam krawędź łączącą wierzchołek i-ty z t
#istnieje kilku (n) sąsiadów umożliwiających dotarcie do t pokonując najkrótszą drogę:
#wtedy uruchamiam drugiego bfsa, zaczynając od wierzchołka t, do kolejki dodaję jedynie te wierzchołki, dla których d[u] == d[v]-1,
#Kończę w momencie, gdy w kolejce pozostaje jeden element: jeżeli jest to s, to zwracam None, wpp wykonuje powyższą procedurę dla tego wierzchotka

def bfs(G,s,t,d):
    Q = deque()
    visited = [False for i in range (len(G))]
    Q.append(s)
    visited[s]=True
    d[s] = 0
    while (Q):
        v = Q.popleft()
        for u in G[v]:
            if visited[u] == False:
                Q.append(u)
                visited[u] = True
                d[u] = d[v]+1

def bfs_f(G,s,t,d):
    Q = deque()
    visited = [False for i in range (len(G))]
    Q.append(t)
    visited[t]=True
    while (True):
        v = Q.popleft()
        for u in G[v]:
            if visited[u] == False:
                if(d[u] == d[v]-1):
                    Q.append(u)
                    visited[u] = True
        if(len(Q)==1): return(Q.pop())

def bfs_check(G,s,t,d):
    min = 0
    index = None
    while (t != s):
        min = 0
        if len(G[t]) == 1: 
            return (t, G[t][0])

        for i in G[t]:
            if d[i] == d[t] - 1:
                min+=1
                index = i

        if(min > 1):
                t = bfs_f(G,s,t,d)
                if t == s : return None
        else: return (index, t)


def longer( G, s, t ):
    d = [inf for i in range (len(G))]
    bfs(G,s,t,d)
    if (d[t]==inf): return None
    return bfs_check(G,s,t,d)
    
#G = [[1,4,6],[0,2],[1,3],[2,5,7],[0,5],[4,3],[0,7],[6,3]]
#s = 0
#t = 3
#print (longer(G,s,t))

runtests( longer, all_tests = True)
