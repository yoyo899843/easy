#!/usr/bin/env python3
import os
from Crypto.Cipher import AES
from base64 import b64decode

key = os.urandom(16)

def decrypt(text):
    iv, text = text[:16], text[16:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(text)

with open("flag", 'r') as data:
    flag = data.read().strip()

print("===== Welcome to number game =====")

answer = int.from_bytes(os.urandom(16), 'big')

while True:
    number = decrypt(b64decode(input("guess : ").strip()))[:16]
    number = int.from_bytes(number, 'big')
    if number > answer: print("Too big")
    elif number < answer: print("Too small")
    else: print(flag)
