#!/bin/sh
#exec 2>/dev/null
cd /home/ctf
PYTHONWARNINGS="ignore:not adding directory '' to sys.path" timeout 10 ./server.sage
