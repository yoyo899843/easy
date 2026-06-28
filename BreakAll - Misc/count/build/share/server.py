#!/usr/bin/env python3

print("===== Welcome to counting game =====")
print("You just need to count from 1 to 100 and get the flag")
print("I will help you, just repeat after me")

for i in range(1, 100 + 1):
    print("----- wave {}/100 -----".format(i))
    print("I say {} you say?".format(i))
    x = int(input().strip())
    if x != i:
        print("Wrong! You suck!")
        exit(0)

with open('./flag') as f:
    print(f.read().strip())
