#!/usr/bin/env python3
import os

FLAG = open('./flag', 'r').read()

def season_encode(byte):
    binary_string = bin(byte)[2:].zfill(8)
    seasons = ['A', 'B', 'C', 'D']
    encoded = ""
    
    for i in range(0, 8, 2):
        pattern = binary_string[i:i+2]
        if pattern == '00':
            encoded += seasons[0]
        elif pattern == '01':
            encoded += seasons[1]
        elif pattern == '10':
            encoded += seasons[2]
        else:  # '11'
            encoded += seasons[3]
    
    return encoded

def main():
    res = ''
    for char in FLAG:
        res += season_encode(ord(char)) + ' '
    print(res.strip())

try :
    main()
except : 
    print("error detected")