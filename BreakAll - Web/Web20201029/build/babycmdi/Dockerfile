FROM php:7.3-apache
MAINTAINER RB363
RUN apt update
RUN apt install iputils-ping -y

WORKDIR /var/www/html

COPY index.php .
COPY flag_e06087052920a5e14b7fb1a40bc799dfe6d46a19 .

RUN chmod 755 ./ && chgrp root ./ && chown root ./ 
RUN chmod 644 index.php && chgrp root index.php && chown root index.php 
RUN chmod 644 flag_e06087052920a5e14b7fb1a40bc799dfe6d46a19
RUN chgrp root flag_e06087052920a5e14b7fb1a40bc799dfe6d46a19
RUN chown root flag_e06087052920a5e14b7fb1a40bc799dfe6d46a19

CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
