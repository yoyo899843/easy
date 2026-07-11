#!/usr/bin/env python3
import random
import string

print("===== Welcome to alphabet counter =====")
print("We got some alphabet to count")
print("Can you help us?")

for i in range(100):
    print("----- wave {}/100 -----".format(i + 1))
    ch = chr(ord('a') + random.randint(0, 25))
    text = ''.join([random.choice(string.ascii_lowercase) for _ in range(50)])
    print('How many {} in {}'.format(ch, text))
    x = int(input().strip())
    if not (x == text.count(ch)):
        exit(9)

print("CTF{m4rvel AGeNts 0F ShIE1d - 41pHab3t CouNter}")
