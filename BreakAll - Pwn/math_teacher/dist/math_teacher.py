#!/usr/bin/env python3
import signal
import sys
import random


def handler(signum, frame):
    print('\nMath teacher get angry. ヽ(#`Д´)ﾉ')
    sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.alarm(60)

for i in range(100):
    x = random.randint(-128, 127)
    y = random.randint(-128, 127)
    a1 = random.randint(1, 10)
    b1 = random.randint(1, 10)
    c1 = a1 * x + b1 * y
    a2 = random.randint(1, 10)
    b2 = random.randint(1, 10)
    c2 = a2 * x + b2 * y
    print('{} * x + {} * y = {}'.format(a1, b1, c1))
    print('{} * x + {} * y = {}'.format(a2, b2, c2))
    try:
        x = int(input('x = '))
        y = int(input('y = '))
    except Exception as e:
        print('OMG! hacker!!')
        sys.exit()
    if x * a1 + y * b1 != c1 and x * a2 + y * b2 != c2:
        print('Wrong answer!')
        sys.exit()

# print flag
with open('flag') as f:
    print(f.read())
