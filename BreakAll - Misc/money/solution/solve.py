#!/usr/bin/env python3
from pwn import *
import string

r = remote('127.0.0.1', 20000)

r.recvlines(8)

for i in range(100):
    r.recvuntil('money : ')
    money = int(r.recvline().strip())
    r.recvuntil('interest : ')
    interest = int(r.recvline().strip().strip(b'%'))
    r.sendlineafter('answer : ', str(money + money // 100 * interest))

r.interactive()
