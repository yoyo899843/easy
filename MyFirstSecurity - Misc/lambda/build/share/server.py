#!/usr/bin/env python3
import random

print("===== Welcome to lambda =====")
print("give you x, help us calculate f(x)")
print("here is some functions f")
print("f0(x) = 3x^2 + x + 3")
print("f1(x) = 5x^2 + 8")
print("f2(x) = 4x^3 + 6x + 6")
print("f3(x) = 7x^3 + 5x^2")
print("f4(x) = x^2 + 4x + 3")

F = [lambda x: 3 * (x ** 2) + x + 3,
     lambda x: 5 * (x ** 2) + 8,
     lambda x: 4 * (x ** 3) + 6 * x + 6,
     lambda x: 7 * (x ** 3) + 5 * (x ** 2),
     lambda x: x ** 2 + 4 * x + 3]

print("----- wave : example -----")
print("function : 1")
print("x = 2")
print("f(x) = 28")

for i in range(100):
    print("----- wave : {}/100 -----".format(i + 1))
    f = random.randint(0, 4)
    x = random.randint(0, 1000)
    print("function : {}".format(f))
    print("x = {}".format(x))
    fx = int(input().strip())
    if F[f](x) != fx:
        print("WRONG...")
        exit(0)

print("MyFirstCTF{R0gUe on3 - A st4r wARs LamBd4}")
