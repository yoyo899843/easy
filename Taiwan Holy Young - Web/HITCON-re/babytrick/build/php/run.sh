#!/bin/sh

service apache2 start

service mysql start
mysql -uroot -pPr0ph3t < /var/www/init.sql


/bin/bash