from Crypto.Util.number import *

p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221
n = p * q
e = 65537

flag = open('./flag', 'rb').read()


m = bytes_to_long(flag)
c = pow(m, e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')