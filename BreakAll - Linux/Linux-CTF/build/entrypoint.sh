#!/bin/bash
echo "$FLAG" > /home/lab/flag
chown lab:lab /home/lab/flag
chmod 644 /home/lab/flag
exec /usr/sbin/sshd -D
