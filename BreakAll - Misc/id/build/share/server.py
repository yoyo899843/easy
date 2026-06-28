#!/usr/bin/env python3
import random
import string

print("===== Welcome to id identification =====")
print("Can you help me identify these id?")
print("Rule 1 : Must start with a uppercase letter A-Z")
print("Rule 2 : Follow by 9 digits")
print("Rule 3 : Summation of these 9 digits must be divisible by 3")

print("----- Example -----")
print("id : e123456789")
print("answer : invalid")
print("----- Example -----")
print("id : E000000002")
print("answer : invalid")
print("----- Example -----")
print("id : E123456789")
print("answer : valid")

for i in range(1, 100 + 1):
    print(f"----- wave {i}/100 -----")
    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    id = random.choice(upp * 7 + low) + str(random.randint(0, 999999999))
    print(f"id : {id}")
    answer = input("answer : ").strip()
    if len(id) == 10 and id[0] in upp and sum(map(int, id[1:])) % 3 == 0:
        ans = 'valid'
    else:
        ans = 'invalid'
    if answer != ans:
        print("Wrong Answer")
        exit()

with open("./flag") as f:
    print(f.read())
