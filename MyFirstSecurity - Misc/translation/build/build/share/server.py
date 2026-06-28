#!/usr/bin/env python3
import random

print("========== Welcome ==========")
print("I give you a string, you need to translate it to integer in big endian")

print("----- wave : example -----")
print("string : ab (all the string will contain lowercase alphabets only)")
print("integer : 24930 ( which comes from 97 * 256 + 98 = 24930)")

marvel = ['ironman', 'captainamerica', 'wolverine', 'hulk', 'spiderman', 'thor', 'hawkeye', 'blackpanther', 'blackwidow', 'oalieno']

for i in range(100):
    print("----- wave : {}/100 -----".format(i + 1))
    string = marvel[random.randint(0, len(marvel) - 1)]
    print("string : {}".format(string))
    integer = input("integer : ").strip()
    if integer != str(int.from_bytes(string.encode('ascii'), 'big')):
        print("YOU SUCKS...")
        exit(0)

print("MyFirstCTF{stAr m4rVel VII - thE F0rCe AWakeNs}")
