#!/bin/sh
exec 2>/dev/null
cd /home/ctf
timeout 10 ./server.py
