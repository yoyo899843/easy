#!/usr/bin/env sage
import sys
import random

print("===== Welcome to Get the Root =====")
print("I need you to solve some polynomial for me, just give me one of the roots of the polynomial")

print("----- wave : example -----")
print("polynomial : 1 -2 1 (which means x^2 - 2x + 1)")
print("root : 1 (just one of the roots, and gurantee to be integer)")

sys.stdout.flush()

F.<x> = ZZ[]

for i in range(100):
    print("----- wave : {}/100 -----".format(i + 1))
    P = 1
    for _ in range(random.randint(3, 8)):
        P *= (x + random.randint(-100, 100))
    print("polynomial : {}".format(' '.join(map(str, P.list())[::-1])))
    sys.stdout.write("root : ")
    sys.stdout.flush()
    root = int(raw_input().strip())
    if P(root) != 0:
        print("WRONG...")
        exit()

print("MyFirstCTF{RoOt w4rs VIII - th3 L4sT j3dI}")
