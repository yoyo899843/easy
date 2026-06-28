FROM nimmis/apache-php7
#RUN apt-get update

COPY index.php /var/www/html/index.php
COPY bootstrap.css /var/www/html/bootstrap.css
COPY config.php /var/www/html/config.php

RUN rm /var/www/html/index.html
#RUN apachectl start
