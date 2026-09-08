#!/usr/bin/env python3
import sys
import random


def polymul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def polyeval(coeffs, value):  # coeffs low-degree first
    acc = 0
    for c in reversed(coeffs):
        acc = acc * value + c
    return acc


print("===== Welcome to Get the Root =====")
print("I need you to solve some polynomial for me, just give me one of the roots of the polynomial")

print("----- wave : example -----")
print("polynomial : 1 -2 1 (which means x^2 - 2x + 1)")
print("root : 1 (just one of the roots, and gurantee to be integer)")

sys.stdout.flush()

for i in range(100):
    print("----- wave : {}/100 -----".format(i + 1))
    P = [1]
    for _ in range(random.randint(3, 8)):
        P = polymul(P, [random.randint(-100, 100), 1])
    print("polynomial : {}".format(' '.join(map(str, P[::-1]))))
    sys.stdout.write("root : ")
    sys.stdout.flush()
    root = int(input().strip())
    if polyeval(P, root) != 0:
        print("WRONG...")
        exit()

print("MyFirstCTF{RoOt w4rs VIII - th3 L4sT j3dI}")
