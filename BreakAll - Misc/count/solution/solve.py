#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

for i in range(1, 100 + 1):
    r.sendlineafter('you say?\n', str(i))

r.interactive()
