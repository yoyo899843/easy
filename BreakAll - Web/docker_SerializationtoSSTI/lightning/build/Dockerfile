FROM nimmis/apache-php7
#RUN apt-get update

COPY index.php /var/www/html/index.php
COPY flag.php /var/www/html/flag.php
COPY nothing.php /var/www/html/nothing.php

RUN rm /var/www/html/index.html
#RUN apachectl start
