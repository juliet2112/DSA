#1. A i B się przemieszczają, muszą dotrzeć do A' i B', ale tak, ze nie mogą się znaleźć w odległośći mniejszej niż d
#Graf możliwych pozycji A i B (7,3)-(6,8) itd.
#złożoność znajduję odległości każdego do każdego wierzchołka O(V^3)
#wybieram pary elementów O(V^2), pesymistycznie krawędzi rzędu V^4
#da się też zrobić w O(V^3)
#tylko jeden porusza się naraz wtedy krawędzi 2V*V^2 (v^2 wierzchołków pośrednich i v krawędzi po każdej stronie)
# ale skierowne krawędzie i zawsze najpierw się rusza druga współrzędna
#wierzchołków V^3, bo dodajemy wierzchołki pośrednie i robimy bfs

#Mimalne drzewo rozpinające(MST) - Kruskal 
#log*(V)

#api
#make_set() -> Set
#find(x) -> set
#union(x,y)
from math import inf 
def mst(E):
    R = []
    n = -1
    for w,x,y in E:
        n = max(x,y,n)
    n+=1

    S = [make_set() for _ in range (n)]
    E.sort()
    #ewentualnie E = E.sorted()
    for w,x,y in E:
        a = find(S[x])
        b = find(S[y])

        if a != b:
            union(S[x],S[y])
            R.append((w,x,y))

    return R

#cykl o min wadze
#EV^2 dijkstra dla każdej krawędzi
#V^3 floydwarshal, dla każdej pary wierzchołków dodaję odległość z A do B i B do A tylko dla skierowanych

#G=(V,E,W)
#jedzie autobus Alicja i Bob, A ma jechać jak najkrócej
#kto rusza? S-> S(A), S-> S(B) (do kolejki S(A) i S(B) z odległością zero, a potem min z dwóch)
#do kolejki krotka odl,wierzchołek, kto prowadzi

    

        