def pijemy(k, PIWO):
    n = len(PIWO)
    typ = [0 for _ in range (k+1)]
    new = [0 for _ in range (n)]
    maxi = 0
    max_typ = -1

    for i in range (n):
        typ[PIWO[i]]+=1
        if typ[PIWO[i]] > maxi:
            maxi = typ[PIWO[i]]
            max_typ = PIWO[i]

    cur = max_typ
    for i in range (0,n,2):
        if typ[cur] == 0:
            if cur == max_typ:
                cur = 1
                max_typ = -1
            else:
                cur+=1
        if typ[cur] == 0:
            continue
        new[i] = cur
        typ[cur] -= 1

    for i in range (1,n,2):
        if typ[cur] == 0:
            if cur == max_typ:
                cur = 1
                max_typ = -1
            else:
                cur+=1
        if typ[cur] == 0:
            continue
        new[i] = cur
        typ[cur] -= 1
        
    return new
   
"""
Prosimy nie modyfikować kodu poniżej :)
"""

#k = int(input())
#piwo = list(map(int, input().split(" ")))
piwo = [1, 2, 1, 1, 1, 3, 3, 3, 2, 3]
k=3
n = len(piwo)
sol = [k, n] + pijemy(k, piwo)
print(" ".join(str(x) for x in sol))