#!/usr/bin/env python3
import random

print("===== Welcome to Set Challenge =====")
print("Can you help me union these two sets")
print("Print it out in sorted order")

print("----- Example -----")
print("1 4 3 2 5")
print("5 3 9 1 12")
print("answer : 1 2 3 4 5 9 12")

print("----- Now You Turn -----")
A = [random.randint(0, 1000) for _ in range(30)]
B = [random.randint(0, 1000) for _ in range(30)]
print(' '.join(map(str, A)))
print(' '.join(map(str, B)))
answer = input('answer : ').strip()
ans = ' '.join(map(str, sorted(list(set(A) | set(B)))))
if answer == ans:
    print('Accepted')
    with open('./flag') as f:
        flag = f.read()
    print(f'Here is your flag : {flag}')
else:
    print('Wrong Answer')
