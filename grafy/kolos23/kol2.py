from kol2testy import runtests
class Node:
    def __init__(self,val):
        self.parent = self
        self.value = val
        self.rank = 0

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y: return
    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        if(x.rank == y.rank):
            x.rank += 1

def lista_kraw(G):
    E = []
    maxi = 0
    for v in range (len(G)):
        for u,w in G[v]:
            if (v < u):
                if u > maxi:
                    maxi = u
                E.append((v,u,w))
    return E,maxi


def kruskal(E,n,i): 
    G = [Node(i) for i in range (n)]
    suma = 0
    for v,u,w in E[i:i+n-1]:
        if find(G[v]) == find(G[u]):
            return -1
        union(G[v],G[u])
        suma+=w
    return suma

def beautree(G):
    E,n = lista_kraw(G)
    E.sort(key=lambda E: E[2])
    for i in range(len(E)-n):
        mini = kruskal(E,n+1,i)
        if mini != -1:
            return mini
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)