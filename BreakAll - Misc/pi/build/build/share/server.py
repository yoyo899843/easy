#!/usr/bin/env python3
import sympy
import random

print("===== Welcome to pi calculator =====")
print("give me pi with certain length")
print("----- wave example -----")
print("L = 5")
print("3.1415")

for i in range(100):
    print("----- wave {}/100 -----".format(i + 1))
    L = random.randint(2, 100)
    print("L = {}".format(L))
    x = input().strip()
    if x != str(sympy.N(sympy.pi, L)):
        exit(0)

print('CTF{THE HUngeR GAMES - moCKINGJAY}')
