#!/usr/bin/env python3
import random

print("===== emag gnitros ot emocleW =====")
print("Can you sort these alphabets in reverse order(z-a)?")

print("----- Example -----")
print("word : python")
print("answer : ytponh")

words = """
better
perform
cross
sheet
coach
gleaming
callous
damaging
determined
present
uttermost
helpful
sort
describe
shoes
loud
radiate
borrow
well-groomed
guide
weak
cultured
mother
ripe
waste
astonishing
bawdy
hum
alert
wide
sack
advice
godly
neighborly
scarecrow
expensive
class
control
provide
mourn
slip
judicious
colorful
yarn
cub
self
book
rob
greet
recognise
glow
mend
pull
strap
bolt
include
sick
petite
zealous
faded
oval
gun
sticky
visit
bee
sudden
summer
stale
exist
happen
pump
jazzy
rampant
soda
rub
elite
suck
abounding
short
square
change
church
front
enthusiastic
full
act
pipe
bomb
knowing
proud
wool
pancake
argument
sturdy
tow
ashamed
expect
cent
chess
spare
"""
words = words.split()

for i in range(1, 100 + 1):
    print(f"----- wave {i}/100 -----")
    word = random.choice(words)
    print(f"word : {word}")
    ans = input("answer : ")
    if ans != ''.join(sorted(word))[::-1]:
        print("Wrong Answer")
        exit()

with open('./flag') as f:
    print(f.read())
