#O(nlogn)
#Tworzę drzewo binarne minimum i przechowuję wszystkie potencjalnie potrzebne magazyny
#Za każdym razem, gdy dodaję nowy transport szukam liścia najbardziej na lewo, do którego mogę zmieścić transport i zwracam jego indeks
from egz2atesty import runtests
def depth(x):
    s = 1
    cnt = 0
    while s < x:
        s*=2
        cnt+=1
    return cnt

class BinTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.min = 0
        self.id = None

    def buildtree(self,num):
        d = depth(num)
        i = 0
        def addnodes(node,x):
            nonlocal i
            if x > 0:
                node.left = BinTree()
                node.right = BinTree()
                addnodes(node.left,x-1)
                addnodes(node.right,x-1)
            else:
                node.id = i
                i+=1
        addnodes(self,d)


    def addvalue(self,x,T):
        def edit(node,x):
            nonlocal T
            i = None
            if not node.left:
                node.min = node.min + x
                return node.id
            if node.left.min + x <= T:
                i = edit(node.left,x)
            elif node.right.min + x <= T:
                i = edit(node.right,x)

            node.min = min(node.left.min,node.right.min)
            return i
            
        return edit(self,x)




def coal( A, T ):
    Tree = BinTree()
    Tree.buildtree(len(A))
    last = None
    for v in A:
        last = Tree.addvalue(v,T)
    return last

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True)