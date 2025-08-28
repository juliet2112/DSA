from collections import deque

def dwudzielny(G):
    Q = deque()
    kolor = [0 for i in range (len(G))]

    for v in range (len(G)):
        if kolor[v] == 0:
            kolor[v] = 1
            Q.append(v)
            while Q:
                v = Q.popleft()
                for u in G[v]:
                    if kolor[u] == 0:
                        kolor[u] = -kolor[v]
                        Q.append(u)
                    if kolor[u] == kolor[v]: return False
    
    return True

G = [[1,2],[0,2,3,5],[0,1,4,6],[1,5,6],[2,5,8],[1,3,5],[2,3,7],[6,8],[4,7]]
#G = [[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[0,2,4],[]]
print(dwudzielny(G))
