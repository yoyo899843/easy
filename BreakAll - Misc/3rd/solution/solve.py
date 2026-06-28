#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(7)

r.recvuntil('numbers : ')
numbers = map(int, r.recvline().strip().split())
ans = sorted(numbers)[-3]
r.sendlineafter('answer : ', str(ans))

r.interactive()
