#O(n^3logn)
#Wybieram wszystkie możliwe podciągi,
#sortuję je i usuwam elementy, które zaniżają wartość podciągu, zwracam maksimum

from egz1btesty import runtests
from math import inf

def kstrong( T, k):
  n = len(T)
  maxi = -inf
  for p in range (n):
    for r in range (p,n):
      pom = T[p:r+1]
      pom.sort()
      wynik = sum(pom)
      for i in range (k):
        if i < len(pom) and pom[i] < 0:
          wynik -= pom[i]
        else:
          break
      if wynik > maxi:
        maxi = wynik

  return maxi




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )