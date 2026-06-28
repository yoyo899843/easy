# beautify

### 類型

PPC

### 題目敘述

#### English

Can you help me beautify these sentences?

Rule 1 : change all ' -_' to ' '

Rule 2 : change all alphabet to lower case

`nc xxx.xxx.xxx yyy`

#### 中文

幫我美化一下這句子

規則一 : 把所有 ' -_' 換成 ' '

規則二 : 把所有英文字母換成小寫

nc xxx.xxx.xxx yyy

### FLAG

CTF{NoWYoUKNoWhOWt0STRinG}

### 架設題目

啟動服務

```shell
docker-compose up -d
```

關閉服務

```shell
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

### 檔案

 題目的壓縮檔中包含數個檔案

- README.md : 此份檔案 ( markdown 格式 )
- README.pdf : 此份檔案 ( pdf 格式 )
- image : 包含 dockerfile
- share : 包含 server.py 程式碼以及 flag
- solve.py : 解答程式碼 ( 預設連接 127.0.0.1:20000 )