#stacje benzynowe
#mamy stacje w pozycjach x1,...,xn i ceny paliwa c1,...,cn
#jak tankujemy to zawsze do pełna, a jeśli zatrzymujemy się na stacji, to musimy zatankować

#tworzymy wierzchołki opisujące w jakiej stacji jesteśmy i ile mamy paliwa w baku
#krawędzie opisujące tankowanie i spalanie paliwa

#graf O(nlog(nL) + n^2) <- lepsza złożoność
#dynamicznie O(nL^2)

#f(i,x) - najtańszy koszt dojechania do stacji i-tej, tak by mieć x paliwa w baku
#i - numer stacji, do której chcemy dojechać, x - stan paliwa w baku

#f(x,i) = min(f(i-1,l) [0,L-1] + ci-1(L-l), (jeśli x=L-(di-di-1) else inf) lub f(i-1, x+(di-1 -di))

#na zachłanne bierzemy gorszą strategię i poprawiamy ją jako dowód poprawności

#jeżeli nie ma tańszej stacji to jedziemy do pierwszej stacji O(n^2)

#