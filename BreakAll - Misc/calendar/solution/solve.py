#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(9)

for i in range(100):
    r.recvuntil('year : ')
    year = int(r.recvline().strip().decode())
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
    r.sendlineafter('answer : ', ["ordinary", "leap"][ans])

r.interactive()
