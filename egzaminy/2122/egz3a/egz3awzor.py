from egz3atesty import runtests
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

        
def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )