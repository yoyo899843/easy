# pi

### 類型

PPC

### 題目敘述

#### English

Help me calculate pi.

nc xxx.xxx.xxx yyy

#### 中文

幫我算算圓周率

nc xxx.xxx.xxx yyy

### FLAG

CTF{THE HUngeR GAMES - moCKINGJAY}

### 架設題目

啟動服務

```shell
cd build
docker-compose up -d
```

關閉服務

```shell
cd build
docker-compose down
```

預設的開的 port 是 20000

可在 build/docker-compose.yml 中更改

```yaml
...
ports:
    - "20000:9999"
...
```

### 解答

用 sympy 套件

```Python
from sympy import *
N(pi, 10)
```

完整代碼請見 : solve.py

### 註記

 題目的壓縮檔中包含數個檔案

- pi.md : 此份檔案 ( markdown 格式 )
- pi.pdf : 此份檔案 ( pdf 格式 )
- build : 架設題目的檔案 ( 包含 source code )
- solve.py : 解答程式碼 ( 預設連接 127.0.0.1:20000 )