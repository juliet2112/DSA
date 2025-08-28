# Czy G - skierowany ma "uniwersalne ujście" - wierzchołek, taki, że:
# 1) nie da się wyjść z niego
# 2) z każdego innego wierzchołka jest krawędź.

# Wszystkie na niego wskazują, a on na żaden.

# Reprezentacja macierzowa (da się na niej tutaj rozwiązać lepiej niż O(n^2))

# Dla każdego wierzchołka sprawdzam stopień wejściowy i wyjściowy.
# Złożoność O(|V|)

def universalne(G):
    n = len(G)
    i,j = 0,0
    while i < n and j < n:
        if G[i][j] == 0:
            j+=1
        else:
            i+=1
            j = 0

    if i == n: return False

    for k in range (n):
        if k != i:
            if G[k][i] == 0: return False

    return True




G = [
    [0,1,1,0],
    [1,0,0,1],
    [0,0,0,0],
    [1,0,1,0]
    ]
print(universalne(G))