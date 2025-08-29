#O(E+V)
#BFS wieloźródłowy, który zapisuje dla każdego wierzchołka z którego zainfekowanego grzybem jest do niego najbliżej
#Na koniec sumujemy wierzchołki oznaczone grzybem d
#Priorytet mają grzyby o najniższych indeksach, bo jako pierwsze dodajemy je do kolejki bfs
from egz3atesty import runtests
from collections import deque
from math import inf

def bfs1(G,T):
    n = len(G)
    Q = deque()
    d = [[inf,None] for _ in range(n)]
    for s in T:
        d[s][0] = 0
        d[s][1] = s
        Q.append(s)

    while Q:
       v = Q.popleft()
       for u in G[v]:
            if d[v][0]+1 < d[u][0]:
                d[u][0] = d[v][0]+1
                d[u][1] = d[v][1]
                Q.append(u)
    return d

  
def mykoryza(G,T,d):
    n = len(G)
    dist = bfs1(G,T)

    cnt = 0
    for i in range (n):
        if dist[i][1] == T[d]:
            cnt+=1

    return cnt

    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True)