from egzP3btesty import runtests 
from queue import PriorityQueue

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
    if x == y: return
    if x.rank < y.rank:
        x.parent = y

    else:
        y.parent = x
        if x.rank == y.rank:
            x.rank +=1
def lista_kraw(G):
    E = []
    suma = 0
    for v in range (len(G)):
        for u, w in G[v]:
            if v < u:
                E.append((v,u,w))
                suma += w
    return E,suma

def kruskal(G):
    E,prev = lista_kraw(G)
    aft = 0
    maxi = None
    E.sort(key=lambda x: x[2], reverse=True)
    nodes = [Node(i) for i in range(len(G))]

    for v, u, w in E:
        if find(nodes[v]) != find(nodes[u]):
            union(nodes[v], nodes[u])
            aft+=w
        elif maxi == None:
            maxi = w 

    return prev - (aft+maxi)

def lufthansa ( G ):
    return kruskal(G)
    

runtests ( lufthansa, all_tests=True )