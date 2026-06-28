# lambda

### 類型

PPC

### 題目敘述 ( English )

Help me calculate some functions

nc xxx.xxx.xxx yyy

### 題目敘述 ( 中文 )

幫我算一些函式吧

nc xxx.xxx.xxx yyy

### FLAG

MyFirstCTF{R0gUe on3 - A st4r wARs LamBd4}

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

總共一百關，給 x 要計算 f(x)

總共有五個固定的函式 f0, f1, f2, f3, f4

使用匿名函式可以輕鬆解出

```python
lambda x: x + 1
```

完整代碼請見 : solve.py

### 註記

 題目的壓縮檔中包含數個檔案

- lambda.md : 此份檔案 ( markdown 格式 )
- lambda.pdf : 此份檔案 ( pdf 格式 )
- build : 架設題目的檔案 ( 包含 source code )
- public : 公開給參賽者在賽中下載的原始碼或資料
- solve.py : 解答程式碼 ( 預設連接 127.0.0.1:20000 )