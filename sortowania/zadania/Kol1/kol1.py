from kol1testy import runtests
#Julia Jamorska
#Wykorzystuję algorytm bucketsort, aby posortować listę palików, gdyż rozmieszczone są zgodnie z rozkładem jednostajnym
#Paliki wewnątrz przedziałów sortuję wykorzystując algorytm quicksort
#Następnie przechodzę po posortowanej tablicy, jednocześnie porównując odległości każdych dwóch sąsiednich palików
#Liczę ile jest takich sąsiednich palików o odległości pomiędzy >= D
#Złożoność czasowa: bucketsort O(n) + przejście po tablicy T O(n), czyli złożoność: O(n + n) = O(n)
#Złożoność pamięciowa: pesymistycznie chyba O(n^2), bo tworzę wiaderka, ale dla rozkładu jednostajnego można założyć, że O(n)

def partition(A,p,r):
  #wybieram środkowy element jako pivota i zamieniam go miejscem z ostatnim
  pivot = (p+r)//2
  A[pivot],A[r] = A[r],A[pivot]
  x = A[r]
  i = p - 1
  for j in range (p,r):
    if A[j] <= x:
      i+=1
      A[i],A[j] = A[j],A[i]

  A[i+1],A[r] = A[r],A[i+1]
  return i+1
  
def quicksort(A,p,r):
  while p < r:
    q = partition(A,p,r)
    quicksort(A,p,q-1)
    p=q+1


#Dzielę przedział (0,M) na len(T)//5 przedziałów i dodaję do nich odpowiednie elementy
#Następnie scalam przedziały w posortowaną tablicę
def bucketsort(T,M):
    n = len(T)
    numb = n//4

    #powstaje jeden przedział
    if(numb == 0):
       quicksort(T,0,len(T)-1)
       return
    
    zak = M/numb
    Buckets = [[] for i in range(numb+1)]

    for i in range(n):
        Buckets[int(T[i] / zak)].append(T[i])

    for i in range(numb):
        quicksort(Buckets[i], 0, len(Buckets[i]) - 1)

    # scalanie przedziałów
    k = 0
    for i in range(numb):
        for j in Buckets[i]:
            T[k] = j
            k += 1

def ogrodzenie(M, D, T):
  n = len(T)
  ile = 0
  bucketsort(T,M)

  #zliczenie palików o odległości pomędzy >= D
  for i in range (1,n):
     if(T[i]-T[i-1] >= D):
        ile+=1

  return ile

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True)
