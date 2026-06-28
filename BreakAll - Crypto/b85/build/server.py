import base64
import string
import random

def custom_encode(text):
    text_bytes = text.encode('utf-8')
    base85_encoded = base64.b85encode(text_bytes).decode('utf-8')
    result = ''
    random.seed(2024)
    for i in range(len(base85_encoded)):
        result += base85_encoded[i]
        if i % 3 == 2:
            result += random.choice('!@#$%^&*')
    
    return result

flag =open('./flag', 'r').read()
encoded_flag = custom_encode(flag)
challenge_description = f"""
{encoded_flag}
"""

print(challenge_description)