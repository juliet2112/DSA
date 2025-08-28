def zeroFilledSubarray(nums):
    def count(x):
        if x in cnt:
            return cnt[x]
        if x == 0:
            return 0
        wynik = count(x-1)+x
        cnt[x] = wynik
        return wynik

    ile = 0
    zeros = 0
    cnt = {}
    for x in nums:
        if x == 0:
            zeros+=1
        else:
            ile += count(zeros)
            zeros = 0

    if zeros != 0:
        ile += count(zeros)

    return ile

T = [0,0,0,2,0,0]
print(zeroFilledSubarray(T))