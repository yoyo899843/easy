#!/usr/bin/env python3
import string
import random

def shift(text, s):
    ans = ""
    for c in text:
        if c in string.ascii_letters:
            base = ord('a') if c >= 'a' else ord('A')
            c = ord(c) - base
            c = (c + s + 26) % 26
            c = chr(base + c)
        ans += c
    return ans
        
lines = ["THE MAN WHO PASSES THE SENTENCE SHOULD SWING THE SWORD",
         "THE THINGS I DO FOR LOVE",
         "THE NEXT TIME YOU RAISE A HAND TO ME WILL BE THE LAST TIME YOU HAVE HANDS",
         "IT'S THE FAMILY NAME THAT LIVES ON. IT'S ALL THAT LIVES ON",
         "WHEN YOU PLAY THE GAME OF THRONES, YOU WIN OR YOU DIE",
         "I LEARNED HOW TO DIE A LONG TIME AGO",
         "WHEN DEAD MEN AND WORSE COME HUNTING ... YOU THINK IT MATTERS WHO SITS ON THE IRON THRONE",
         "THE MAD KING DID AS HE LIKED. HAS YOUR UNCLE JAIME EVER TOLD YOU WHAT HAPPENED TO HIM",
         "TURN US AWAY, AND WE WILL BURN YOU FIRST",
         "A GIRL GIVES A MAN HIS OWN NAME"]

print("Hurry up, winter is coming...")

template = "shift every alphabet in the word by {:+} : {}"

for i in range(100):
    print("===== wave {}/100 =====".format(i + 1))
    s = random.randint(-25, 25)
    i = random.randint(0, len(lines) - 1)
    print(template.format(s, shift(lines[i], -s)))
    user = input().strip()
    if user != lines[i]:
        print("You have been crushed by Mountain...")
        exit(0)

print("MyFirstCTF{sTaR w4rs VI - RetUrn 0f thE jOn SNoW}")
