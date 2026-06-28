#!/usr/bin/env python3
from pwn import *
import string

r = remote('127.0.0.1', 20000)

r.recvlines(14)

for i in range(100):
    r.recvuntil('id : ')
    id = r.recvline().strip().decode()
    if len(id) == 10 and id[0] in string.ascii_uppercase and sum(map(int, id[1:])) % 3 == 0:
        ans = 'valid'
    else:
        ans = 'invalid'
    r.sendlineafter('answer : ', ans)

r.interactive()
