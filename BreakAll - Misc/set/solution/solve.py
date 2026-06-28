#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(8)
A = map(int, r.recvline().decode().strip().split(' '))
B = map(int, r.recvline().decode().strip().split(' '))
ans = ' '.join(map(str, sorted(list(set(A) | set(B)))))
r.sendlineafter('answer : ', ans)

r.interactive()
