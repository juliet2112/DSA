#Pause - ćw.8 2021

# malejące krawędzie - ćw.8 2021
#nie zaznaczamy wierzchołków w dfs, nie wchodzimy do wierzchołków o większych wagach

#bezpieczny przelot,
#sortowanie krawędzi po długościach i odpalanie bfsu

#ścieżka hamiltona w dagu

#dobry początek

#cykl eulera w reprezentacji macierzowej
#linearyzacja tablicy (przy przechowywaniu wartości pod przekątną)

def EulerCycle2(G, s):
    n = len(G)
    euler = []
    index = [0] * n # visited edges po prostu

    def EulerVisit2(G, u):
        while index[u] < n:
            v = index[u]
            index[u] = v + 1
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                EulerVisit2(G, v)
                euler.append(u)

    euler.append(s)
    EulerVisit2(G, s)

    return euler

#Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. 
#Każde miasto jest otoczone murem i ma tylko dwie bramy—północną i południową. 
# Z każdej bramy prowadzi dokładnie jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też być połączone drogami między sobą). 
# Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą, to musi go opuścić drugą. 
# Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta zakaz formułowania zadań “o szachownicy” (obraza majestatu). 
# Szach chce, żeby goniec odwiedził każde miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). 
# Goniec wyjeżdża ze stolicji Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić (bez implementacji) algorytm, który stwierdza czy odpowiednia trasa gońca istnieje. 
# Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność czasową.

#szukanie cyklu eulera