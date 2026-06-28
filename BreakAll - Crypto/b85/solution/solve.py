import base64

def custom_decode(encoded_text):
    """
    自定義解碼過程:
    1. 移除混淆字符
    2. Base85解碼
    3. 轉換回文本
    """
    # 步驟1: 移除混淆字符
    clean_text = ''
    for i, char in enumerate(encoded_text):
        if i % 4 != 3:  # 跳過每第4個字符（混淆字符）
            clean_text += char
    
    # 步驟2: Base85解碼
    decoded_bytes = base64.b85decode(clean_text)
    
    # 步驟3: 轉換回文本
    return decoded_bytes.decode('utf-8')

print(custom_decode("Vsd*3+Y#hi3%`dv$#xP&bz^%8>W$o~0*{WN^B_^&Uu|$J?b%Y*g^V"))