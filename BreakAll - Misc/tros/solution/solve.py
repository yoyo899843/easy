#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(5)

for i in range(100):
    r.recvuntil('word : ')
    word = r.recvline().strip().decode()
    ans = ''.join(sorted(word))[::-1]
    r.sendlineafter('answer : ', ans)

r.interactive()
