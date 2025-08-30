#O(nlogn)
#Sortuję po przedziały po początkach i dodaję je kolejno na kopiec min po końcach
#Usuwam jednoczenie wszystkie przedziały, które kończą się przed początkiem obecnie sprawdzanego przedziału - tj. są z nim i wszystkimi kolejnymi rozłączne
#Jeżeli pozostaje jakiś przedział na kopcu to sprawdzam cz aktualnie sprawdzany jest z nim niefajny
from egz3btesty import runtests
from heapq import heappop,heappush

def uncool( P ):
    n = len(P)
    for i in range(n):
        P[i].append(i)

    P.sort(key = lambda x: x[0])
    T = [[P[0][1],P[0][0],P[0][2]]]
    for i in range (1,n):
        pair = P[i]
        while T and T[0][0] < pair[0]:
            heappop(T)
        if T and T[0][1] < pair[0] and T[0][0] < pair[1]:
            return ((T[0][2],pair[2]))
        heappush(T,[pair[1],pair[0],pair[2]])
        
  


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True)

"""for a,b,c in T:
            if b < pair[0] and a < pair[1]:
                return ((c,pair[2]))"""