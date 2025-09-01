#O(n)
#Najpierw ustalam wyskość każdego podrzewa
#Sprawdzam na którym jest najwięcej liści i ile krawędzi muszę obciąć, by nie było lisci poniżej tego poziomu
#W odtatnim dfsie liczę ile krawędzi muszę obciąć, by nie było liści powyżej tego poziomu
from egz1btesty import runtests
from math import inf
class Node:
    def __init__( self ):
        self.left = None    # lewe poddrzewo
        self.right = None   # prawe poddrzewo
        self.x = None
    
def seth(node,val):
    if not node:
        return
    node.x = val
    seth(node.left,val+1)
    seth(node.right,val+1)

def maxh(node):
    if not node:
        return -inf
    maxi = node.x
    maxi = max(maxi,maxh(node.left),maxh(node.right))
    return maxi

def findnum(node):
    def find(a):
        if not a:
            return
        T[a.x]+=1
        if a.x != 0:
            cuts[a.x - 1]+=1
        find(a.left)
        find(a.right)
            
    T = [0 for _ in range (maxh(node)+1)]
    cuts = [0 for _ in range (maxh(node)+1)]
    find(node)
    return T,cuts
    
def dfs(node, h):
    ile = 0
    def dfsvisit(node):
        nonlocal h
        nonlocal ile
        if not node:
            return -inf
        odp1 = dfsvisit(node.left)
        odp2 = dfsvisit(node.right)
        if odp1 != -inf and odp2 != -inf:
            if odp1 >= h and odp2 < h or odp2 >= h and odp1 < h:
                ile +=1
        return max(odp1,odp2,node.x)

    dfsvisit(node)
    return ile
        

def wideentall( T ):
    seth(T,0)
    Nums,cuts = findnum(T)
    n = len(Nums)
    maxi = 0
    maxid = 0
    for i in range (n-1,-1,-1):
        if Nums[i] > maxi:
            maxi = Nums[i]
            maxid = i

    return cuts[maxid] + dfs(T,maxid)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )