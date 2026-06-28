#!/usr/bin/env python3
import sympy
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(5)

for _ in range(100):
    r.recvline()
    exec(r.recvline().strip())
    r.sendline(str(sympy.N(sympy.pi, L)))

r.interactive()
