FROM dockerfiles/centos-lamp 
#RUN apt-get update
#RUN yum install -y gcc

COPY index.php /var/www/html/index.php
COPY mysql.sql /mysql.sql
COPY flag /flag

RUN sed -i "s/Indexes//g" /etc/httpd/conf/httpd.conf

