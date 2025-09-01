# kol1testy.py
from testy import *
from kol3test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)

def printarg(T):
    B, C, s = T
    print("\nOpis blatu\t: ", limit(B))
    print("Sumy czastkowe\t: ", limit(C))
    print("Limit sęków\t: ", s)


def printhint( hint ):
    print("\nWynik poprawny         : ", hint)


def printsol( sol ):
    print("Wynik algorytmu        : ", sol, end="\n\n")


def check( T, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    newtest = {}
    B = [[2, 1, 4], [1, 3, 1], [2, 3, 3]]
    C = [[20, 15, 8], [13,  10, 4], [8,  6, 3]]
    s = 5
    newtest["arg"] = [B, C, s]
    newtest["hint"] = 4
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

