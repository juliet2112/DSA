def numberOfWays(T):
        chair = 0
        cnt = 1
        cnt_pom = 1
        for i in range (len(T)):
            if T[i] == 'S':
                chair+=1

            if chair == 2:
                i+=1
                while i < len(T) and T[i] == 'P':
                    cnt_pom+=1
                    i+=1
                if i < len(T):
                    cnt*=cnt_pom
                    cnt_pom = 1
                    chair = 0

        if chair == 1:
            return 0

        else:
            return cnt%(10**9 + 7)

T = "S"
print(numberOfWays(T))