from collections import deque

# kolejka na dwóch stosach
input = []
output = []
def put(el):
    input.append(el)
def get(el):
    if output.empty():
        while not input.empty():
            output.append(input.pop())
    return output.pop()

#następnik w drzewie bst
#gdy ma prawego syna, to jest to min w jego poddrzewie
#wpp idziemy w górę, aż będziemy w lewym poddrzewie
#dla największego el cofamy się aż dojdziemy do korzenia

#modyfikacja drzewa bst, tak aby istniała możliwość znalezienia i-tego co do wielkości elementu
#idziemy do min i 5 razy szukamy następnika O(n)
#dodajemy do wierzchołków liczbę el w lewym poddrzewie

#dwudzielność grafu
def dwudzielny(G): #G w postaci listy sąsiedztwa
    Q = deque()
    kolor = [0 for i in range (len(G))]

    for v in range (len(G)):
        if kolor[v] == 0:
            kolor[v] = 1
            Q.append(v)
            while Q:
                v = Q.popleft()
                for u in G[v]:
                    if kolor[u] == 0:
                        kolor[u] = -kolor[v]
                        Q.append(u)
                    if kolor[u] == kolor[v]: return False
    
    return True

G = [[1,2],[0,2,3,5],[0,1,4,6],[1,5,6],[2,5,8],[1,3,5],[2,3,7],[6,8],[4,7]]
#G = [[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[0,2,4],[]]
print(dwudzielny(G))

#liczba spójnych składowych w grafie
def dfs(G):
    def dfsvisit(G,v):
        visited[v] = True
        for u in G[v]:
            if visited[u] == False:
                dfsvisit(G,u)

    visited = [False for i in range (len(G))]
    skladowe = 0
    for v in range (len(G)):
        if visited[v] == False:
            skladowe+=1
            dfsvisit(G,v)
    
    return skladowe


G = [[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[0,2,4],[]]
print(dfs(G))

#cykl długości 4
#bierzemy każdą parę wierzchołków i sprawdzamy czy istnieją dwa wierzchołki połączone z nimi 

#uniwersalne ujście
#jak znaleźć wiersz z samymi zerami w czasie O(n)