#!/usr/bin/env python3
import random
from fractions import Fraction

print("===== Welcome =====")
print("I need you to transform from Fahrenheit to Celsius")

print("----- wave : example -----")
print("Fahrenheit : 10 (guarantee to be integer)")
print("Celsius : -110/9")

for i in range(100):
    print("----- wave : {}/100 -----".format(i + 1))
    F = random.randint(-100, 100)
    print("Fahrenheit : {}".format(F))
    C = Fraction(*list(map(int, input("Celsius : ").strip().split('/'))))
    if (C * 9 / 5) + 32 != Fraction(F, 1):
        print("WRONG")
        exit(0)

print("MyFirstCTF{h4rRy potTer anD tHe phiL0sOph3r's TeMper4tuRe}")
