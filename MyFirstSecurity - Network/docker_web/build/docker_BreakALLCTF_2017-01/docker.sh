#!/bin/bash
cd web-1
docker build -t breakallctf-2017-01-web-1 .
docker run -p 1001:80 -d breakallctf-2017-01-web-1