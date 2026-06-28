#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(1)

counts = [(3, 2, 2, 2, 2, 2, 3), (1, 2, 2, 1, 1, 1, 5), (5, 2, 1, 5, 1, 1, 7), (5, 2, 1, 5, 1, 2, 5), (1, 2, 2, 2, 7, 1, 1), (7, 1, 1, 6, 1, 2, 5), (5, 2, 1, 6, 2, 2, 5), (7, 2, 1, 1, 1, 1, 1), (5, 2, 2, 5, 2, 2, 5), (5, 2, 2, 6, 1, 2, 5)]

for i in range(1, 100 + 1):
    r.recvlines(3)
    count = tuple(r.recvline().count(b'#') for _ in range(7))
    ans = counts.index(count)
    r.sendlineafter('What is this digit? ', str(ans))

r.interactive()
