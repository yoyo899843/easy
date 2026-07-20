FROM dockerfiles/centos-lamp 
#RUN apt-get update
#RUN yum install -y gcc

RUN yum -y install mod_ssl;exit 0

COPY index.php /var/www/html/index.php
COPY user.sql /user.sql
COPY mysql.sql /mysql.sql


RUN sed -i "s/Indexes//g" /etc/httpd/conf/httpd.conf

# 要把user.sql, mysql.sql匯入
# RUN cat /user.sql | mysql -uroot
# RUN cat /mysql.sql | mysql -uroot
