FROM php:7.3-apache
MAINTAINER RB363
RUN apt update

WORKDIR /var/www/html

COPY index.php .
COPY config.php .

CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
