FROM php:7.0-apache
MAINTAINER RB363
RUN apt update

WORKDIR /var/www/html

COPY index.php .
COPY flag_fd9fcddf524d2ebfd53a66cb0422570da5c3efcc .

RUN chmod 755 ./ && chgrp root ./ && chown root ./ 
RUN chmod 644 index.php && chgrp root index.php && chown root index.php 
RUN chmod 644 flag_fd9fcddf524d2ebfd53a66cb0422570da5c3efcc
RUN chgrp root flag_fd9fcddf524d2ebfd53a66cb0422570da5c3efcc
RUN chown root flag_fd9fcddf524d2ebfd53a66cb0422570da5c3efcc

RUN echo "error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING" >> /usr/local/etc/php/php.ini

CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
