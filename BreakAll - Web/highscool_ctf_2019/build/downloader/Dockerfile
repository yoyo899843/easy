FROM nimmis/apache-php7
#RUN apt-get update

COPY index.php /var/www/html/index.php
COPY config.inc.php /var/www/html/config.inc.php
COPY download.php /var/www/html/download.php
COPY cute1.jpg /var/www/html/cute1.jpg
COPY cute2.jpg /var/www/html/cute2.jpg
COPY cute3.png /var/www/html/cute3.png

RUN rm /var/www/html/index.html
#RUN apachectl start
