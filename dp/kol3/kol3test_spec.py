from testy import MY_random, MY_modulus

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (3, 3, 8, 2, 1, 3),
    (6, 6, 12, 3, 1, 8),
    (6, 6, 12, 5, 0.8, 6),
    (30, 30, 80, 6, 0.0053, 52),
    (40, 80, 9931, 10, 0.103, 109),
    (100, 101, 891, 1, 0.37, 198),
    (300, 400, 921, 16, 0.683, 683),
    (800, 800, 2323, 88, 0.555, 1511),
    (900, 1000, 30461, 3, 0.301, 1895),
    (1000, 1000, 291821, 101, 0.331, 1872),
]

def gendesk(desklen, s, density):
    rand = float(MY_random()) / MY_modulus
    rand_density = density + rand * (1 - density)
    sval = round(s * rand_density)
    dividers = [MY_random() % (sval + 1) for _ in range(desklen - 1)]
    dividers.append(0)
    dividers.append(sval)
    dividers.sort()
    arr = []
    for i in range(1, len(dividers)):
        arr.append(dividers[i] - dividers[i-1])
    return arr

def gentest(n, m, s, initlen, density, hint):
    B = [[0]  * m for _ in range(n)]
    C = [[0]  * m for _ in range(n)]

    row = n
    col = m

    initside = 'r' if MY_random() % 2 == 0 else 'c'
    initdesk = gendesk(initlen, s, density)
    if initside == 'r':
        row = n - 1
        col = m - len(initdesk)
        for i in range(len(initdesk)):
            B[row][col + i] = initdesk[i]
    else:
        row = n - len(initdesk)
        col = m - 1
        for i in range(len(initdesk)):
            B[row + i][col] = initdesk[i]

    while row > 0 or col > 0:
        side = 'r' if row > 0 else 'c'
        if row > 0 and col > 0:
            side = 'r' if MY_random() % 2 == 0 else 'c'

        if side == 'r':
            desk = gendesk(m - col, s, density)
            row -= 1
            for i in range(len(desk)):
                B[row][col + i] = desk[i]
        else:
            desk = gendesk(n - row, s, density)
            col -= 1
            for i in range(len(desk)):
                B[row + i][col] = desk[i]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            C[i][j] += B[i][j]
            if i < n-1:
                C[i][j] += C[i+1][j]
            if j < m-1:
                C[i][j] += C[i][j+1]
            if i < n-1 and j < m-1:
                C[i][j] -= C[i+1][j+1]

    return (B, C, s), hint
