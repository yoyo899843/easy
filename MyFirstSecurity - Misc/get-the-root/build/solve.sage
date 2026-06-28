#!/usr/bin/env sage
import socket

class remote:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.buffer = ""
    def recvuntil(self, text):
        while text not in self.buffer:
            self.buffer += self.s.recv(1)
        index = self.buffer.find(text) + len(text)
        ans, self.buffer = self.buffer[:index], self.buffer[index:]
        return ans
    def recvline(self):
        return self.recvuntil('\n')
    def recvlines(self, n):
        ans = ""
        for _ in range(n):
            ans += self.recvline()
        return ans
    def send(self, text):
        self.s.sendall(text)
    def sendline(self, text):
        self.s.sendall(text + '\n')

F.<x> = ZZ[]

r = remote('127.0.0.1', 20000)

r.recvlines(5)

for _ in range(100):
    r.recvline()
    r.recvuntil("polynomial :")
    P = F(map(int, r.recvline().strip().split())[::-1])
    r.sendline(str(P.roots()[0][0]))

print r.recvline()
