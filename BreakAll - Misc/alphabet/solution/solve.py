#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(3)

for i in range(100):
    r.recvline()
    r.recvuntil('How many ')
    ch = r.recvn(1)
    r.recvuntil(' in ')
    text = r.recvline().strip()
    r.sendline(str(text.count(ch)))

r.interactive()
