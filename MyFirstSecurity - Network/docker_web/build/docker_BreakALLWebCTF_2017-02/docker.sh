#!/bin/bash
cd web-1
docker build -t breakallwebctf-2017-02-web-1 .
docker run -p 2001:80 -d breakallwebctf-2017-02-web-1
cd ../web-2
docker build -t breakallwebctf-2017-02-web-2 .
docker run -p 2002:80 -e MYSQL_PASS="securitylab" -d breakallwebctf-2017-02-web-2
cd ../web-3
docker build -t breakallwebctf-2017-02-web-3 .
docker run -p 2003:80 -d breakallwebctf-2017-02-web-3
cd ../web-4
docker build -t breakallwebctf-2017-02-web-4 .
docker run -p 2004:80 -d breakallwebctf-2017-02-web-4
cd ../web-5
docker build -t breakallwebctf-2017-02-web-5 .
docker run -p 2005:80 -d breakallwebctf-2017-02-web-5