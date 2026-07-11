FROM php:7.3-apache
MAINTAINER RB363
RUN apt update

WORKDIR /var/www/html

COPY index.php .
COPY flag_f9ef43c66b4d8ed8d93081d96fc16202d6f20e8d.txt .

RUN echo "error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING" >> /usr/local/etc/php/php.ini
RUN mkdir upload/
RUN chmod 777 upload/
RUN chmod 755 ./ && chgrp root ./ && chown root ./ 
RUN chmod 644 index.php && chgrp root index.php && chown root index.php 
RUN chmod 644 flag_f9ef43c66b4d8ed8d93081d96fc16202d6f20e8d.txt 
RUN chgrp root flag_f9ef43c66b4d8ed8d93081d96fc16202d6f20e8d.txt 
RUN chown root flag_f9ef43c66b4d8ed8d93081d96fc16202d6f20e8d.txt 

CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
