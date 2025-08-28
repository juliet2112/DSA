def dijkstra(G,s,w):
    n = len(G)
    visited = [(0,0) for _ in range (n)]
    d = [(inf,inf) for _ in range(n)]
    PQ = PriorityQueue()
    state = 0
    PQ.put((G(s),s,state))

    while not PQ.empty():
        dist, v, state = PQ.pop()
        if (state == 0 and visited[v][0]) == 1 or (state == 1 and visited[v][1] == 1): 
            continue
        if dist > max(d[v][0],d[v][1]):
            continue

        if v == w:
             return min(d[v][0],d[v][1])

        for u in range (n):
            w1 = G[v][u]
            if d[v][state] + w1 < d[u][0]:
                    d[u][0] = d[v][state] + w1
                    PQ.put((w1,u,(state+1)%2))
            if state == 0:
                for z in range(n):
                     w2 = max(w1, G[u][z])
                     if d[z][1] > d[v][state] + w2:
                          d[z] = d[v][state] + w2
                          PQ.put((w2,z,(state+1)%2))


def dijkstra_matrix(s,G,w):
    n = len(G)
    #state: 0 - wchodzę bez butów, 1 - z butami
    d = [(inf,inf) for _ in range (n)]
    parent = [None for _ in range (n)]
    visited = [False for _ in range (n)]

    d[s] = 0
    cur_state = 0
    while True:
        min_dist = inf
        min_index = -1
        for i in range (n):
            if G[i] < min_dist and visited[i] == False:
                min_dist = d[i]
                min_index = i
                
        if min_index == -1:
            return d
        
        visited[min_index] = True

        for v in range(len(G[min_index])):
            if d[v][0] > d[min_index][cur_state] + G[min_index][v]:
                d[v][0] = d[min_index][cur_state] + G[min_index][v]
                parent[v] = min_index

