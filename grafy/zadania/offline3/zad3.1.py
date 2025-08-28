from zad3testy import runtests
from collections import deque
from math import inf

#Za pomocą algorytmu bfs wyznaczam najkrótszą drogę z s do każdego z wierzchołków
#Sprawdzam jaka jest odległość sąsiadujących z t wierzchołków od s
#jeżeli d[t] = inf, to połączenie nie istnieje
#Rozpartuję trzy przypadki:
#t ma tylko jednego sąsiada: wtedy przechodzę do tego sąsiada (t = G[t][0]) , aby połączenie z wierzchołkiem t nadal istniało i rozpoczynam szukanie dla tego wierzchołka
#tylko jeden z sąsiadów (i-ty) umożliwia dotarcie do t pokonując najkrótszą drogę (d[i] = d[t]-1), wtedy usuwam krawędź łączącą wierzchołek i-ty z t
#istnieje kilku (n) sąsiadów umożliwiających dotarcie do t pokonując najkrótszą drogę, wtedy możliwe są dwa przypadki:
#a) nie da się usunąć krawędzi tak, by wydłużyć drogę (wtedy przechodząc do sąsiada coraz to bliższego s w końcu dotrzemy do s (warunek końcowy s==t))
#b) części 

#bfs w jedną i w drugą i porównywanie od s i t
#

def dfs(G,s,t,d):
    def DFSvisit(G,v):
        nonlocal time

        children = 0

        times[v] = time
        low[v] = time
        time +=1

        for u in G[v]:
            if times[u] == inf:
                parent[u] = v
                children +=1
                low[v] = min(low[v],DFSvisit(G,u))

                if parent[v] == None and children > 1:
                    aps_t[v] = True

                elif low[u] >= d[v]:
                    aps_t[v] = True

            elif u != parent[v]:
                low[v] = min(low[v], times[u])

        if low[v] == times[v] and parent[v] != None:
            bridges.append((v,parent[v]))

        return low[v]

    time = 0
    low = [inf for i in range (len(G))]
    times = [inf for i in range (len(G))]
    parent = [None for i in range(len(G))]
    aps_t = [False for i in range(len(G))]
    aps = []
    bridges=[]

    DFSvisit(G,s)

    for i in range(len(G)):
        if aps_t[i]:
            aps.append(i)

    return bridges, aps


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

def bfs_check(G,s,t,d):
    min = 0
    index = None
    czy = False 

    while (t != s):

        if len(G[t]) == 1: 
            return(t, G[t][0])    

        for i in G[t]:
            if d[i] == d[t] - 1:
                min+=1
                index = i



        if(min > 1):
            if czy == False:
                bridges,aps = dfs(G,s,t,d)
                cur_aps = len(aps)
                czy = True

            if len(bridges) != 0 :
                return bridges[0]
            
            t = aps[cur_aps - 1]
            cur_aps -= 1
                
        else: 
            return (index, t)


def longer( G, s, t ):
    d = [inf for i in range (len(G))]
    bfs(G,s,t,d)
    if (d[t]==inf): 
        return None
    return bfs_check(G,s,t,d)
    
#G = [[1,4],[0,2],[1,3],[2,5],[0,5],[4,3],[0,7],[6,3]]
#s = 0
#t = 3
#print (longer(G,s,t))
runtests( longer, all_tests = True)