#O(n)
#W secie przechowuję wszystkie liczby k-pechowe z zakresu <k,n>
#prechodzę tablicę równocześnie przechowując indeksy 3 ostatnich liczb k-pechowych
#szukam najdłuższego przedziału

from egz3btesty import runtests

def num(k,n):
    x = {k}
    ile = 1
    while k < n:
        k = k + (k%ile) + 7
        x.add(k)
        ile+=1
    return x

def kunlucky(T, k):
    n = len(T)
    nums = num(k,n)
    maxx = 0
    k3 = None
    k1 = None
    k2 = None
    for i in range (n):
        if T[i] in nums:
            if k1 != None:
                if maxx == 0:
                    maxx = i
                else:
                    maxx = max(maxx, i-k1-1)
            k1 = k2
            k2 = k3
            k3 = i

    maxx = max(maxx, n-k1-1)

    return maxx  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True)