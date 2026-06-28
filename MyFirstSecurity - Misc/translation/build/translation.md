# translation

### 類型

PPC

### 題目敘述 ( English )

I need you to translate string to integer for me

nc xxx.xxx.xxx yyy

### 題目敘述 ( 中文 )

我需要你幫忙把字串轉成整數

nc xxx.xxx.xxx yyy

### FLAG

MyFirstCTF{stAr m4rVel VII - thE F0rCe AWakeNs}

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

總共一百關，要將字串用 big endien 轉成整數

使用 python3 中內建函式  `int.from_bytes(string, 'big')`

完整代碼請見 : solve.py

### 註記

 題目的壓縮檔中包含數個檔案

- translation.md : 此份檔案 ( markdown 格式 )
- translation.pdf : 此份檔案 ( pdf 格式 )
- build : 架設題目的檔案 ( 包含 source code )
- public : 公開給參賽者在賽中下載的原始碼或資料
- solve.py : 解答程式碼 ( 預設連接 127.0.0.1:20000 )