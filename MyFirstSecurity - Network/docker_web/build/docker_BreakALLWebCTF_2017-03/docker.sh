#!/bin/bash
cd web-1
docker build -t breakallwebctf_2017-03-web-1 .
docker run -p 3001:80 -d breakallwebctf_2017-03-web-1
cd ../web-2
docker build -t breakallwebctf_2017-03-web-2 .
docker run -p 3002:80 -d breakallwebctf_2017-03-web-2
cd ../web-3
docker build -t breakallwebctf_2017-03-web-3 .
docker run -p 3003:80 -d breakallwebctf_2017-03-web-3
cd ../web-4
docker build -t breakallwebctf_2017-03-web-4 .
docker run -p 3004:80 -d breakallwebctf_2017-03-web-4
cd ../web-5
docker build -t breakallwebctf_2017-03-web-5 .
docker run -p 3005:80 -d breakallwebctf_2017-03-web-5