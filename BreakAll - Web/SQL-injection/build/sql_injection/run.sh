#!/bin/bash
set -e

service mysql start

until mysqladmin ping --silent; do
    sleep 1
done

mysql -uroot < /user.sql
mysql -uroot < /mysql.sql

exec apache2-foreground
