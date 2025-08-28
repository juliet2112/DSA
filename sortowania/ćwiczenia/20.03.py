#implementacja iteracyjna quicksorta

def quicksort(A,p,r):
    stack = [(0,r)]
    while stack:
        p,r = stack.pop()
        while p < r:
            q = partition(A,p,r)
            if q - p < r - q:
                stack.append((q + 1,r))
                r = q-1
            else:
                stack.append((p,q-1))
                p = q+1


#partition hoara
#nie działa

def partition(T,l,r):
    i = l
    j = r
    pivot = T[(l+r)//2]
    while True:
        while T[i] < pivot:
            i+=1
        while T[j] > pivot:
            j-=1
        if i >= j:
            return j
        T[i],T[j]=T[j],T[i]
        i+=1
        j-=1

#ciąg liczb
# T = [2,5,6,8,4,3,1,7,9,1]
#co pod indeksem k w posortowanej tablicy

def quickselect(A,p,r,k):
        while p < r:
            q = partition(A,p,r)
            if q==k: return A[k]
            elif k < q:
                r=q-1
            else:
                p=q+1
        return A[k]

#sortowanie kubełkowe - rozkład jednostajny
#odcinki, granice to liczby całkowite, w każdym odcinku(zbiorze) jednostajny rozkład wyników, co nie dotyczy całości
#posortować całość w O(n)


#dwa słowa a i b długości n, czy są anagramami, czyli tyle samo, takich samych znaków
#A = "bacabcba"
#B = "cabacbac"
# alfabet to k symboli

#zliczamy w tablicy długości k znaki, następnie odejmujemy przechodząc po 2 słowie
#złożoność O(n+k)

#dla bardzo długiego k >> n (tak,aby złożoność nie zależała od k)
# można posortować O(nlogn)
# hashowanie
#mapowanie 0 - b, 1 - a, 2 - c  O(n*c), gdzie c - to liczba różnych symboli
#zliczamy pod indeksami char(T[i]) - dużo pamięci, potem sprawdzamy tylko w tych pozycjach

#dodawanie elementu do kopca
def dodaj(H,x):
    H.append(x)