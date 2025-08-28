#O(n^3)
#Dynamicznie: f[p][k] - minimalny koszt połączenia wszystkich wejść od p do k
# f[p][k] = min(f[p+1][k-1] + abs(T[p]-T[k]), dla każdego i = <p+1,k-1> min(f[p][i]+f[i+1][k]))
# warunki brzegowe: łączymy tylko wejścia na pozycjach parzystych z nieparzystymi: p%2 == k%2 -> inf
#dla wejść obok siebie (p == k-1) -> abs(T[p]-T[k])
from egz2atesty import runtests
from math import inf

def wired( T ):
  n = len(T)
  memo = {}
  def f (p,k):
    nonlocal memo
    nonlocal T
    if (p,k) in memo:
      return memo[(p,k)]
    
    if p == k-1:
      memo[(p,k)] = abs(T[p]-T[k])
      return abs(T[p]-T[k])

    if p%2 == k%2:
      memo[(p,k)] = inf
      return inf
    
    wynik = inf
    for i in range(p + 1, k):
      left = f(p, i)
      right = f(i + 1, k)
      wynik = min(wynik, left + right)
    wynik = min(wynik, f(p+1,k-1) + abs(T[p]-T[k]))
    memo[(p,k)] = wynik

    return wynik

  odp = f(0,n-1)
  return odp+n/2

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )