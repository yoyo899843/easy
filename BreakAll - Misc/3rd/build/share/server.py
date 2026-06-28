#!/usr/bin/env python3
import random

print("===== Welcome to 3rd Game =====")
print("Can you help me find the 3rd largest number?")
print("All numbers are unique")

print("----- Example -----")
print("numbers : 1 9 7 3 6 2")
print("answer : 6")

print("----- Now You Turn -----")
numbers = [i for i in range(100000)]
random.shuffle(numbers)
numbers = numbers[:100]
print(f"numbers : {' '.join(map(str, numbers))}")
answer = int(input("answer : ").strip())
if answer == sorted(numbers)[-3]:
    with open("./flag") as f:
        print(f.read())
else:
    print("Wrong Answer")
