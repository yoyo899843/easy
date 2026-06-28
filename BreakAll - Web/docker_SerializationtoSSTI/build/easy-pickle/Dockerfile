FROM dockerfiles/centos-lamp


COPY index.php /var/www/html/index.php
COPY pickle.py /var/www/html/pickle.py
COPY flag /flag


RUN sed -i "s/Indexes//g" /etc/httpd/conf/httpd.conf

RUN apachectl start
