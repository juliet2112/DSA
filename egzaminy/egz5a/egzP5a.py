from egzP5atesty import runtests 

def inwestor ( T ):
    T.append(0)
    stack = []
    maxx = 0
    for i in range(len(T)):
        while stack and T[i] < T[stack[-1]]:
            h = T[stack.pop()]
            if not stack:
                width = i
            else:
                width = i -stack[-1] - 1

            maxx = max(maxx, h*width)
        stack.append(i)

    return maxx


runtests ( inwestor, all_tests=True)