#mergesort dla listy

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(l1, l2):
    wart = Node()
    start = wart
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            wart.next = l1
            wart = wart.next
            l1 = l1.next
        else:
            wart.next = l2
            wart = wart.next
            l2 = l2.next

    if l1 != None:
        wart.next = l1
    if l2 != None:
        wart.next = l2

    return start.next

def serie(l1):
    if l1 == None:
        return None
    cur1 = l1
    while(cur1 != None):
        if(cur1 <= cur1.next):
            cur1 = cur1.next
        else:
            second = cur1.next
            cur2 = second
            cur1.next = None
        while(cur2 != None):
              while(cur2 <= cur2.next):
                cur2 = cur2.next
        
        if cur2.next == None:
            cur2 = None
    if cur1.next == None:
        cur2 = None
    return head, second, cur2

def merge_sort(head):
    cur = head
    while True:
        st, nd, rd = serie(cur)
        if nd == None:
            return
        while nd != None and rd != None:
            beg, end = merge(nd,rd)
            end.next = rd
            nd,rd = serie(rd)



#scalamy parami, a nie do wcześniej scalonej, żeby złożoność była log n !!!

#posortowana tablica A, wartość x, znaleźć indeksy takie, że A[i] + A[j] == x   
#złożoność liniowa 
def szukanie_liniowe(T,x):
    n = len(T)
    i,j = 0,n-1
    r = T[j]+T[i]
    while True:
        if j < i:
            return -1,-1
        r = T[j] + T[i]
        if(r==x):
            return i,j
        elif r > x:
            i+=1
        elif r < x:
            j-=1

#tablica, czy zawiera lidera, czyli liczbę występującą na ponad połowie pozycji
#T = [3,2,4,3,3,1,3,4,3]
#lider = 3
#sum = 1 - 1
#zmieniamy lidera: lider = 2
#przechodimy jeszcze raz przez tablicę, żeby sprawdzić czy lider istnieje O= 2n

#Największy przedział 
#[a1:b1], [a2:b2], ...
#liczby całkowite i nie zaczynają sie i nie kończą w tym samym miejscu
#znaleźć taki przedział, w którym w całości zawiera się jak najwięcej innych przedziałów

#sortujemy po pierwszym elemencie z pary i po ostatnim
#liczymy ile odcinków skończyło się i zaczęło przed wybranym przez nas odcinkiem -> różnica to odcinki zawierające się
#czas liniowy + sortowanie

#napisać funkcję wstawiającą dowolny element do kopca binarnego
#A (większa od kopca), s (maksymalny indeks elem w kopcu), x (wartość do dodania)