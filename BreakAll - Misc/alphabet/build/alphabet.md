# alphabet

### 類型

PPC

### 題目敘述

#### English

Can you count alphabets ?

nc xxx.xxx.xxx yyy

#### 中文

可以幫我數一下有幾個英文字母嗎 ?

nc xxx.xxx.xxx yyy

### FLAG

CTF{m4rvel AGeNts 0F ShIE1d - 41pHab3t CouNter}

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

給一個英文字母和一串英文

屬這串英文裡有幾個該英文字母

`text.count(ch)`

完整代碼請見 : solve.py

### 註記

 題目的壓縮檔中包含數個檔案

- alphabet.md : 此份檔案 ( markdown 格式 )
- alphabet.pdf : 此份檔案 ( pdf 格式 )
- build : 架設題目的檔案 ( 包含 source code )
- solve.py : 解答程式碼 ( 預設連接 127.0.0.1:20000 )