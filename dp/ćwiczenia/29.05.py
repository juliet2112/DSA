# (a0, a1, a2),(a3, ..)(.,an-2, an-1), (wartości nie muszą być dodatnie)
# podzielony na k podciągów, posumowane wartości podciągów
# wartością podziału jest najmniejsza suma
# uzyskać najmniejszą sumę możliwie największą
# (3,7),(9),(8,2,6,1),(3,5)

#stan pozwalający określić czy juz to rozwiązaliśmy: na ile chce podzielić i co podzielić [   |         |    ]
# min_max(k,i) - wartość najlepszego podziału przedziału <0,i> na k podciągów
#f(i,k) = max [l należy {0,i}] min (f(l,k-1),suma(l+1,i))
#f(i,1) = suma(0,i)
#f(j,k) = -inf, j+1 < k
#O(kn^3)
#da się zrobić O(kn^2) sumy prefikowe
#zrobić iteracyjnie

from math import inf
mem ={}
def suma(A,i,k):
    if mem[(i,k)] in mem:
        return mem[(i,k)]
    if i+1 < k:
        return -inf
    if k == 1:
        return sum(A[0:i+1])
    
    result = -inf
    for l in range(i+1):
        result = min(suma(A,l,k-1),sum(A[l+1:i+1]),result)  

#prom, trzeba zmieścić maksymalnie dużo samochodów na dwóch pasach
#l naturalne, a1,...,an naturalne
# rozwiązanie wielomianowe
#l - pierwsze l metrów lewego pasa promu
#p - pierwsze p metrów prawego pasa promu
#k - pierwsze k pojazdów
#f(l,p,k)- czy da się zapakować k pojazdów na l metrów lewego pasa i p metrów prawego pasa 
#wynik zadania to arg_max [k=0,...,n] f(L,L,k)==True
#f(l,p,k)=f(l-A[k],p,k-1) or f(l,p-A[k],k-1)
#f(l,p,k) = False, l,p <0
#f(l,p,0) = True, l,p >= 0
#rekurencja ze spamiętywaniem

#jezioro a na nim liście, na pierwszym jest żaba, na niektórych jest energia (e0,...,en - może być równe 0),
#wykonanie skoku ma koszt (k0,k1,...,kn)
#nie wolno wykonać skoku dłuższego niż wynosi energia
#f(i,e) = najmniejsza liczba skoków w jaką żaba może dotrzeć na i-ty liść, zachowójąc e energii przed zjedzeniem
#f(i,e) = min [j należy 0,..., i-1] f(j,e+K[j])+1, jeśli e + K[j] >= i-j
#f(i,e) = inf, e + K[j] < i-j