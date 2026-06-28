#!/usr/bin/env python3
import random
import string

print("===== Welcome to money game =====")
print("Can you help me calculate bank interest")
print("Give you total amount of money (will be multiple of 100) and annual interest rate")
print("Give me the total amount of money I will have next year")

print("----- Example -----")
print("money : 10000")
print("interest : 5%")
print("answer : 10500")

for i in range(1, 100 + 1):
    print(f"----- wave {i}/100 -----")
    money = random.randint(0, 10000) * 100
    interest = random.randint(1, 80)
    print(f"money : {money}")
    print(f"interest : {interest}%")
    answer = int(input('answer : ').strip())
    if answer != money + money // 100 * interest:
        print("Wrong Answer")
        exit()

with open("./flag") as f:
    print(f.read())
