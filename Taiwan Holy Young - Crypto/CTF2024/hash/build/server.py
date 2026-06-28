import hashlib

def char_to_sha256(char):
    return hashlib.sha256(char.encode('utf-8')).hexdigest()

flag = open('./flag', 'r').read()


# 對每個字符進行SHA256哈希
hashed_chars = [char_to_sha256(char) for char in flag]

# 打印結果
for i, hashed_char in enumerate(hashed_chars, 1):
    print(f"{hashed_char}")

print()