#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvlines(8)
r.recvuntil('sentence : ')
sentence = r.recvline().strip().decode()
ans = sentence.lower().replace('-', ' ').replace('_', ' ')
r.sendlineafter('answer : ', ans)

r.interactive()
