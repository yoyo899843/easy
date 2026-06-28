from secret import FLAG
import numpy as np

key = list(FLAG)
R = np.random.randint(0,256, size=(64,64)).astype(int)
C = np.zeros((64, 64)).astype(int)

for i in range(64):
    if i == 0 :
        C[:, i] = ((R.T[i] * key[i]) % 256)
    else :
        C[:, i] = (C[:,i-1] + R.T[i] * key[i]) % 256

print(f"R = {R.tolist()}")
print(f"C = {C.tolist()}")