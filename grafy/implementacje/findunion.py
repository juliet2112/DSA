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