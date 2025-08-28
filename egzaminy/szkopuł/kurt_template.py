from math import inf

def kurt(D):
    memo = {}
    def f(a,b,D,wall):
        nonlocal memo
        if (a,b) in memo:
            return memo[(a,b)][wall]
        
        wynik = inf
        wynik_wall = inf

        for i in range (a,-1,-1):
            if D[i][b] == 0:
                wynik = f(i,b,D,)



"""
Prosimy nie modyfikować kodu poniżej :)
"""

n = int(input())
D = []
for _ in range(n):
    D.append(input())
sol = kurt(D)
print(sol)