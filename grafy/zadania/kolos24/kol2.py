from kol2testy import runtests
from math import inf
from collections import deque

def ile_wierzcholow(G):
    maxi = G[0][0]
    for a,b,c in G:
        if a > maxi:
            maxi = a
        if b > maxi:
            maxi = b
    return maxi+1
          
def create_graph(G,n):
    NG = [[] for _ in range (n)]
    for v,u,w in G:
        NG[v].append((u,w))
        NG[u].append((v,w))
    return NG
      
def bfs(G,s,n):
    d = [[inf]*17 for _ in range (n)]
    czas = [0 for _ in range (n)]
    Q = deque()

    d[s] = 0
    Q.append((s,0,d[s]))

    while Q:
        v,tired,cnt = Q.popleft()
        if(cnt > 0):
            Q.append((v,tired,cnt-1))
        else:
            visited[v] = True
            for u,w in G[v]:
                if visited[u] == False:
                    mem = czas[u]
                    if(czas[v]+w > 16):
                        czas[u] = w
                        w += 8
                    else:
                        czas[u] = czas[v] + w

                    if d[v] + w < d[u]:
                        d[u] = d[v] + w
                        Q.append((u,w))
                    else:
                        czas[u] = mem

    return d


def warrior( G, s, t):
  with open("graph.txt", 'w') as f:
    for u, v, w in G:
        f.write(f"{u}-({w})-{v}\n")
  n = ile_wierzcholow(G)
  create_graph(G,n)
  New_graph = create_graph(G,n)
  d = bfs(New_graph,t,n)
  return d[s]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests = True)

