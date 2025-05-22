#1. Problem wydawania reszty
# T = 12, M = {1,4,5}
# Lm(t) = minimalna liczba monet jaką wykorzystujemy, żeby wydać kwotę t
# Lm(t) = min (m nalezy do M) f(t-m) + 1
# Lm(0) = 0
# dla t < 0: f(t) = inf
from math import inf
memory = {}
M = [1,4,5]
def Lm(t):
    if t in memory:
        return memory[t]
    
    if t == 0: return 0
    elif t < 0: return inf

    mini = inf 
    for m in M:
        x = Lm(t-m) + 1
        mini = min(mini,x)
    memory[t]=mini
    return mini

print(Lm(9))

#iteracyjnie
#O(T*M)
def Lm_it(t,M):
    n = t+1
    min_monet = [inf for _ in range (n)]
    min_monet[0] = 0

    for i in range(1,n):
        for m in M:
            if i -m >= 0:
                if min_monet[i] > min_monet[i-m] + 1:
                    min_monet[i] = min_monet[i-m] + 1
    return(min_monet[t])

#podzbiór A = [8,7,9,1,16,31,5] o wartości T=22
# t - liczba do posumowania
# i - używam pierwszych i liczba
# O(A*t)
#s_sum(t,i) = s_sum(t-A[i],i-1) lub s_sum(t, i-1)
#s_sum(0, i) = True
#s_sum(t,i) = False, t!= 0 and i < 0
#s_sum(t,i) = False , t < 0

mem = {}
B = [8,7,9,1,16,31,5]
def s_sum(t,i):
    if (t,i) in mem:
        return mem[(t,i)]
    
    if t == 0: wynik = True
    elif t > 0 and i < 0: wynik = False
    elif t < 0: wynik = False

    else:
        wynik = (s_sum(t-B[i],i-1) or s_sum(t, i-1))
    mem[(t,i)] = wynik
    return wynik


#iteracyjnie
#czy potrzebna dwuwymiarowa tablica?
def s_sum(B,t):
    n = len(B)
    dp = [[False for _ in range (n)] for _ in range(t+1)]
    for i in range (n):
        dp[0][i] = True

    for t in range (1,t+1):
        for i in range (1,n):
            dp[t][i] = dp[t][i-1] or (dp[t-B[i]][i-1] if t-B[i] >= 0 else False)

    return dp[t][n-1]

# (a0, a1, a2),(a3, ..)(.,an-2, an-1), (wartości nie muszą być dodatnie)
# podzielony na k podciągów, posumowane wartości podciągów
# wartością podziału jest najmniejsza suma
# uzyskać najmniejszą sumę możliwie największą
# (3,7),(9),(8,2,6,1),(3,5)

#stan pozwalający określić czy juz to rozwiązaliśmy: na ile chce podzielić i co podzielić [   |         |    ]
# min_max(k,i,j) - wartość najlepszego podziału przedziału <i,j> na k podciągów