class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge (l1,l2):
    new = Node(0)
    pom = new
    while (l1.next != None and l2.next != None):
        if (l1.val <= l2.val):
            pom.next = l1
            l1 = l1.next
            pom = pom.next
        else:
            pom.next = l2
            l2 = l2.next
            pom = pom.next

    if (l1.next != None):
        pom.next = l1

    if (l2.next != None):
        pom.next = l2

    return new.next

def series(l1):
    if l1 == None:
        return None
    lista = l1
    s1 = l1
    prev1 = l1
    pom = l1.next

    while (pom.next != None):
        while(prev1.val < pom.val):
            prev1.next = pom
            pom = pom.next
            prev1 = prev1.next
        s2 = prev1.next
        prev2 = s2
        while(prev2.val < pom.val):
            prev2.next = pom
            pom = pom.next
            prev2 = prev2.next
    
    return (s1,s2,prev2)

def mergesort(l1):
    lista = l1
    prev = Node(0)
    while True:
        st,nd,rd = series(lista)
        if(nd != None):
            prev.next = merge(st,nd)
        lista = rd.next



def tab_to_list(T):
    start = Node(0)
    pom = start
    for i in range (len(T)):
        a = Node(T[i])
        pom.next = a
        pom = pom.next
    return start.next

A = [1,4,5,7,8,12]
B = [2,3,6,9,11,14]

a = tab_to_list(A)
b = tab_to_list(B)

c = merge(a,b)

print("Hello")

