# egz1Btesty.py
from testy import *
from egz1Btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)

def printarg(T):
    V, E = T
    print("\nLiczba pracowników\t: ", V)
    print("Lista delegacji\t: ", limit(E))


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
    newtest["arg"] = [4, [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]]
    newtest["hint"] = 3
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

