FROM php:7.3-apache
MAINTAINER RB363
RUN apt update
RUN docker-php-ext-install exif

WORKDIR /var/www/html

COPY index.php .
COPY .htaccess .
COPY flag_62b40d3251a04780e3e6d581f881d235e5612c8d.txt .

RUN echo "error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING" >> /usr/local/etc/php/php.ini
RUN mkdir upload/
RUN chmod 777 upload/
RUN chmod 755 ./ && chgrp root ./ && chown root ./ 
RUN chmod 644 index.php && chgrp root index.php && chown root index.php 
RUN chmod 644 flag_62b40d3251a04780e3e6d581f881d235e5612c8d.txt
RUN chgrp root flag_62b40d3251a04780e3e6d581f881d235e5612c8d.txt
RUN chown root flag_62b40d3251a04780e3e6d581f881d235e5612c8d.txt
RUN chmod 644 .htaccess && chgrp root .htaccess && chown root .htaccess 

CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
