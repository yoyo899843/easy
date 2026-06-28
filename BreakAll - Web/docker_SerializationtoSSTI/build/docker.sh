#!/bin/bash
cd baby-marshal
docker build -t baby-marshal .
docker run -p 5201:5278 -d baby-marshal
cd ../easy-pickle
docker build -t easy-pickle .
docker run -p 5202:80 -d easy-pickle
cd ../oob_xxe
docker build -t oob_xxe .
docker run -p 5203:80 -d oob_xxe
cd ../ruby-erb
docker build -t ruby-erb .
docker run -p 5204:11111 -d ruby-erb
