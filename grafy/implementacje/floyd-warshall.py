from math import inf as i
def floydwarshall(W):
    S = W
    n = len(W[0])
    for k in range (n):
        for v in range (n):
            for u in range (n):
                S[u][v] = min(S[u][v], S[u][k] + S[v][k])

    return S

G = [
      [0, -4,i, i, i], 
      [i, 0, 4, 5, i], 
      [i, i, 0, 2, i], 
      [i, i, i, 0, 3], 
      [i, i, i, i, 0], 
]

N = floydwarshall(G)
print(N)