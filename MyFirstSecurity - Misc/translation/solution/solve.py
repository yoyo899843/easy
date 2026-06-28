#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(5)

for i in range(100):
    r.recvline()
    r.recvuntil('string : ')
    string = r.recvline().strip()
    r.recvuntil('integer : ')
    r.sendline(str(int.from_bytes(string, 'big')))

r.interactive()
