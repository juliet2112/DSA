from zad6testy import runtests
from math import inf
# f to minimalna suma odległości biurowców z pozycji X[0],...,X[i] do przydzielonych im działek,
# przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji <= Y[j].
def parking(X,Y):
  n = len(X)
  m = len(Y)
  f = [[inf for _ in range (m)] for _ in range (n)]

  f[0][0]=abs(X[0]-Y[0])

  for j in range(1,m-n+1):
    f[0][j] = min(abs(X[0]-Y[j]),f[0][j-1])

  for i in range (1,n):
    for j in range (i,m-n+i+1):
      f[i][j] = min(f[i-1][j-1] + abs(X[i]-Y[j]),f[i][j-1])

  return f[n-1][m-1]
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True)


"""
# f to minimalna suma odległości biurowców z pozycji X[0],...,X[i] do przydzielonych im działek,
# przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji = Y[j].
from zad6testy import runtests
from math import inf
def parking(X,Y):
  n = len(X)
  m = len(Y)
  f = [[inf for _ in range (m)] for _ in range (n)]
  curr_min = [[inf for _ in range (m)] for _ in range (n)]

  curr_min[0][0]=abs(X[0]-Y[0])
  f[0][0] = abs(X[0]-Y[0])

  for j in range(1,m):
    f[0][j] = abs(X[0]-Y[j])
    curr_min[0][j] = min(curr_min[0][j-1], f[0][j])

  for i in range (1,n):
    for j in range (i,m-n+i+1):
      f[i][j] = min(curr_min[i-1][j-1] + abs(X[i]-Y[j]),f[i][j])
      curr_min[i][j] = min(curr_min[i][j-1], f[i][j])

  return curr_min[n-1][m-1]
  """