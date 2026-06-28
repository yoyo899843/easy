#!/usr/bin/env python3
import random

opers = [lambda x, y: x + y,
         lambda x, y: x - y,
         lambda x, y: x * y]

opers_index = {'+': 0, '-': 1, '*': 2}

print("===== Welcome to the magic calculator =====")
print("We got some equations here, but the operator is missing.")
print("Can you help us?")

for i in range(100):
    print("----- wave {}/100 -----".format(i + 1))
    A = random.randint(1, 99)
    B = random.randint(1, 99)
    o = random.randint(0, 2)
    ans = opers[o](A, B)
    print("{} ? {} = {}".format(A, B, ans))
    print("which operator(+/-/*)?", end = ' ')

    o = opers_index.get(input().strip())
    if o is None or opers[o](A, B) != ans:
        print("Your math is bad...")
        exit(0)

print("MyFirstCTF{QLwxhEsyUfKQrYxyEeFe}")
