#!/usr/bin/env python3
from pwn import *
from mt19937predictor import MT19937Predictor

def solve():
    r = remote('localhost', 9003)
    predictor = MT19937Predictor()
    
    # 跳過開場白
    r.recvuntil(b"You need to predict the next number Im think about\n")
    
    # 收集39個512位的隨機數
    print("Collecting random numbers...")
    for i in range(39):
        line = r.recvline().strip().decode()
        print(f"Received line: {line}")  # 調試輸出
        
        try:
            # 使用更穩健的分割方法
            parts = line.split(" = ", 1)  # 最多分割一次
            if len(parts) != 2:
                print(f"Warning: Unexpected line format: {line}")
                continue
                
            num = int(parts[1])
            print(f"Successfully parsed number {i+1}: {num}")
            predictor.setrandbits(num, 512)
            
        except Exception as e:
            print(f"Error processing line {i+1}: {e}")
            print(f"Problematic line: {line}")
            r.close()
            return
    
    # 預測下一個512位的數字
    next_num = predictor.getrandbits(512)
    print(f"\nPredicted next number: {next_num}")
    
    # 發送預測
    r.recvuntil(b"Your guess: ")
    r.sendline(str(next_num).encode())
    
    # 接收結果
    print("\nResult:")
    while True:
        try:
            line = r.recvline()
            if not line:
                break
            print(line.decode(), end='')
        except EOFError:
            break
    
    r.close()

if __name__ == "__main__":
    solve()