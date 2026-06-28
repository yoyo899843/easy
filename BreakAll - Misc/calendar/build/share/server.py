#!/usr/bin/env python3
import random

print("===== Welcome to Calendar Calculator =====")
print("Can you help me determine which year is leap year in Gregorian Calendar?")
print("According to Wikipedia : Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.")

print("----- Example -----")
print("year : 2019")
print("answer : ordinary")
print("----- Example -----")
print("year : 2020")
print("answer : leap")

for i in range(1, 100 + 1):
    print(f"----- wave {i}/100 -----")
    year = random.randint(1000, 3000)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                ans = 1
            else:
                ans = 0
        else:
            ans = 1
    else:
        ans = 0

    print(f"year : {year}")
    answer = input("answer : ").strip()
    if ["ordinary", "leap"].index(answer) != ans:
        print("Wrong Answer")
        exit()

with open('./flag') as f:
    print(f.read())
