#Julia Jamorska
#cut(i,j) - wyznacza najmniejszą liczbę cięć deski od punktu (i,j) do końca
#wyznaczamy ją jako min { cut(i-1,j), cut(i,j-1)}
#przypadkiem granicznym jest ten, kiedy nie musimy ciąć dalej deski, bo ma już akceptowalną liczbę sęków i odpowiednie wymiary
#Złożoność O(nm) czasowa i pamięciowa

from kol3testy import runtests
from math import inf

def parkiet(B, C, s):
    memo = {}

    def cut (i,j,C,s):
        if (i,j) in memo:
            return memo[(i,j)]

        if C[i][j] <= s and (len(C)-i == 1 or len(C[0])-j == 1):
            return 0
    
        wynik1 = inf
        if j+1 < len(C[0]) and C[i][j] - C[i][j+1] <= s:
            wynik1 = cut(i,j+1,C,s) + 1

        wynik2 = inf
        if i+1 < len(C) and C[i][j] - C[i+1][j] <= s:
            wynik2 = cut(i+1,j,C,s) + 1

        wynik = min(wynik1, wynik2)
        memo[(i,j)] = wynik
        return wynik
    return cut (0,0, C,s)

runtests(parkiet, all_tests = True)

"""#Julia Jamorska
#cut(i,j) - wyznacza najmniejszą liczbę cięć deski od punktu (i,j) do końca
#wyznaczamy ją jako min { cut(i-1,j), cut(i,j-1)}
#przypadkiem granicznym jest ten, kiedy nie musimy ciąć dalej deski, bo ma już akceptowalną liczbę sęków
#Złożoność O(nm)

from kol3testy import runtests
from math import inf

def parkiet(B, C, s):
    memo = {}

    def cut (i,j,C,s):
        if (i,j) in memo:
            return memo[(i,j)]

        if C[i][j] <= s:
            return 0
    
        wynik1 = inf
        if j+1 < len(C[0]) and C[i][j] - C[i][j+1] <= s:
            wynik1 = cut(i,j+1,C,s) + 1

        wynik2 = inf
        if i+1 < len(C) and C[i][j] - C[i+1][j] <= s:
            wynik2 = cut(i+1,j,C,s) + 1

        wynik = min(wynik1, wynik2)
        memo[(i,j)] = wynik
        return wynik
    return cut (0,0, C,s)"""
