#!/usr/bin/env python3
from pwn import *

def season_decode(season_string):
    seasons = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}
    binary_string = ""
    
    for season in season_string:
        binary_string += seasons[season]
    
    return chr(int(binary_string, 2))

r = remote("127.0.0.1", 9002)

enc = r.recvline().decode().strip()
print("Encoded flag:", enc)

decoded_flag = ""
for encoded_char in enc.split():
    decoded_flag += season_decode(encoded_char)

print("Decoded flag:", decoded_flag)