#!/usr/bin/env python3
from pwn import *

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

r = remote("127.0.0.1", 20000)

r.recvline()

for i in range(100):
    r.recvline()
    line = r.recvline().decode('utf-8')
    s, cipher = line.split(':')
    cipher = cipher.strip()
    s = int(s[35:].strip())
    plain = shift(cipher, s)
    r.sendline(plain)

r.interactive()
