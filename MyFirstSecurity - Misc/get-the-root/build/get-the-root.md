# get the root

### 類型

PPC

### 題目敘述 ( English )

Can you calculate the roots of a polynomial?

nc xxx.xxx.xxx yyy

### 題目敘述 ( 中文 )

你會計算多項式的根嗎?

nc xxx.xxx.xxx yyy

### FLAG

MyFirstCTF{RoOt w4rs VIII - th3 L4sT j3dI}

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

總共一百關，要計算多項式的根

使用 sage 來計算多項式的根

```python
F.<x> = ZZ[]
(x^2 - 2*x + 1).roots()
```

完整代碼請見 : solve.sage

### 註記

 題目的壓縮檔中包含數個檔案

- get-the-root.md : 此份檔案 ( markdown 格式 )
- get-the-root.pdf : 此份檔案 ( pdf 格式 )
- build : 架設題目的檔案 ( 包含 source code )
- public : 公開給參賽者在賽中下載的原始碼或資料
- solve.sage : 解答程式碼 ( 預設連接 127.0.0.1:20000 )