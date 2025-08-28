#liczba porównań = n(1 + 2 + 3 + ... + n) = n(1+n)/2
#liczba przypisań -> zależy od danych wejściowych
#sortowanie stabilne np. 4' przed 4"
def przez_wybieranie(tab):
    n=len(tab)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if (tab[j] < tab[min]):
                min = j
        tab[i],tab[min] = tab[min],tab[i]

#szukanie min i max ze zoptymalizowaną liczbą porównań, złożoność O((3/2)*n)
def min_max(T):
    min_g =T[0]
    max_g =T[0]
    for i in range(0,len(T)-1,2):
        if(T[i]>T[i+1]):
            if(T[i]>max_g): max_g=T[i]
            if(T[i+1]< min_g): min_g=T[i] 
        else:
            if(T[i+1]>max_g): max_g=T[i+1]
            if(T[i]< min_g): min_g=T[i] 
        return(min_g,max_g)

def przez_wstawienie(T):
    for i in range (2,len(T)):
        for j in range (i):
            if(T[i]<T[j]):
                T[i],T[j]=T[j],T[i]

#szukanie w tablicy indeksów i i j, o różnicy równej x
#drugiego szukamy binarnie
def bin_search(x,T):
    b = len(T)- 1
    a = 0
    while(a<b):
        mid = (a+b)//2
        if(x == T[mid]):
            return mid
        elif(x > T[mid]):
            a = mid + 1
        else:
            b = mid
    return(-1)

def szukaj(T,x):
    N = len(T)-1
    for i in range(0,N):
        ij = bin_search(x+T[i],T)
        if(ij != -1):
            return(i,ij)
        
    return(-1,-1)

T = [2,5,8,14,17,18,19]
x=9

print(szukaj(T,x))

#szukamy liniowo dwoma indeksami -> jeśli za mało to w prawo, a za dużo w lewo

def szukanie_liniowe(T,x):
    n = len(T)
    i,j = 0,1
    r = T[j]-T[i]
    while True:
        r = T[j] - T[i]
        if(r==x):
            return i,j
        elif r>x:
            i+=1
        elif r < x:
            j+=1
        elif j >= n:
            return -1,-1
        
#odwracanie listy
def odrw(head):
    prev,cur = None,head
    while cur != None:
        tem = cur.next
        cur.next = prev
        prev,tem = tem,prev
    return prev

#posortowany ciąg liczb A, len(A)=n,   zakres 0,...,m,  m > n, szukamy brakującego indeksu A[i]!=i binarnie
#liniowo porównujemy liczbę z indeksem (aż szkoda czasu to pisać)
#lub bin_search -> szukamy min indeksu z różną liczbą