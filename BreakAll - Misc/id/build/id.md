# id

### 類型

PPC

### 題目敘述

#### English

Can you help me identify these id?

Rule 1 : Must start with a uppercase letter A-Z
Rule 2 : Follow by 9 digits
Rule 3 : Summation of these 9 digits must be divisible by 3

`nc xxx.xxx.xxx yyy`

#### 中文

可以幫我辨識這些 id 嗎

規則一 : 開頭會是大寫的英文字母 A-Z
規則二 : 後面接著 9 個數字
規則三 : 9 個數字的總和要是 3 的倍數

`nc xxx.xxx.xxx yyy`

### FLAG

CTF{tHeSEcrEtoFID}

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