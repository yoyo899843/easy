#!/usr/bin/env python3
import time

print("===== Welcome to CTF =====")
print("You successfully reach this problem")
print("Congratulation!!!")
print("Wait for a few second, let me get you the flag")
print("", flush = True)

time.sleep(3)

with open('./flag') as f:
    flag = f.read()

print(f'Here you go : {flag}')
