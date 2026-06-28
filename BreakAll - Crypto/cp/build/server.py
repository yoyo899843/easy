charset = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!{}@#$%^&()_"

def extended_caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char in charset:
            idx = charset.index(char)
            new_idx = (idx + shift) % len(charset)
            result += charset[new_idx]
        else:
            result += char
    return result

flag = open('./flag', 'r').read()

shift = 17 
encrypted_flag = extended_caesar_encrypt(flag, shift)

challenge_description = f"""
Caesar cipher is too simple so I developed a Caesar cipher PRO
alphabet set: {charset}

flag: {encrypted_flag}
"""
# 生成測試數據
print(challenge_description)
