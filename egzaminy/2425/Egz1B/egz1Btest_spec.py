from testy import MY_random, MY_modulus
ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (5, 6, 4),
    (11, 20, 12),
    (31, 120, 55),
    (211, 600, 504),
    (503, 10000, 1529),
    (1009, 50001, 3020),
    (2003, 200000, 5870),
    (3001, 200000, 11268),
    (4001, 250000, 16092),
    (5003, 900000, 16457),
]


def gentest(V, E, hint):
    from testy import MY_random

    ids = list(range(V))

    def my_random_shuffle(arr):
        for i in range(len(arr)):
            j = MY_random() % len(arr)
            arr[i], arr[j] = arr[j], arr[i]

    my_random_shuffle(ids)

    def random_ordered_pair():
        x = MY_random() % V
        y = MY_random() % V
        while x == y:
            y = MY_random() % V
        return min(x, y), max(x, y)

    pairs = set()
    limit = V * V
    while len(pairs) < E and limit > 0:
        r = random_ordered_pair()
        pairs.add(r)
        limit -= 1

    if len(pairs) != E:
        print("Unable to generate enough unique edges, it is best to use prime numbers for V to avoid repeating edge cycles")
        exit(1)

    edges = []
    for (a, b) in pairs:
        edges.append((ids[a], ids[b]))

    return (V, edges), hint
