#O(nlogn)
#Wykorzystuję sumy prefixowe: czyli do pierwszego elementu dodaję +1, i do pierwszego po nim -1, a następnie sumuję po kolei
#Aby zredukować złożoność z O(n+T) (T może być bardzo duże) do O(nlogn)
#tworzę tablicę przechowującą jedynie krańce przedziałów, czyli o wielkości maksymalnie 2n i sortuję ją w czasie O(nlogn)
from egz3atesty import runtests

def snow( T, I ):
    S = set()
    for a,b in I:
        S.add(a)
        S.add(b)

    Tab = []
    for v in S:
        Tab.append(v)

    Tab.sort()

    memo = {}
    for i in range(len(Tab)):
        memo[Tab[i]] = i

    pom = [0 for _ in range(len(Tab)+1)]
    for a,b in I:
        pom[memo[a]]+=1
        pom[memo[b]+1]-=1

    maxi = pom[0]
    for i in range(1,len(pom)):
        pom[i] += pom[i-1]
        maxi = max(pom[i],maxi)

    return maxi









# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True)