import random
from secret import FLAG
from Crypto.Util.number import bytes_to_long, long_to_bytes

for i in range(50) :
    flagnum = bytes_to_long(FLAG)
    noise = int(''.join(random.choices(['0', '1'], weights=(80, 20), k=len(FLAG)*8)),2)
    print(long_to_bytes(flagnum ^ noise).hex())
