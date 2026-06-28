FROM dockerfiles/centos-lamp 
#RUN apt-get update
#RUN yum install -y gcc

RUN yum -y install mod_ssl;exit 0

COPY flag /flag.xml
COPY index.php /var/www/html/index.php
COPY bootstrap.min.css /var/www/html/bootstrap.min.css

RUN sed -i "s/Indexes//g" /etc/httpd/conf/httpd.conf

RUN apachectl start
