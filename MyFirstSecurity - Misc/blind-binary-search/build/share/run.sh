#!/bin/sh
exec 2>/dev/null
cd /home/ctf
timeout 300 ./server.py
