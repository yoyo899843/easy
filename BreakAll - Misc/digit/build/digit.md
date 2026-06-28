# digit

### 類型

PPC

### 題目敘述

#### English

Can you recognize these digits?

`nc xxx.xxx.xxx yyy`

#### 中文

你辨識的出這些數字嗎?

nc xxx.xxx.xxx yyy

### FLAG

CTF{n0WYouc4nSee}

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