FROM nimmis/apache-php7
#RUN apt-get update

COPY index.php /var/www/html/index.php
COPY bootstrap.css /var/www/html/bootstrap.css
COPY hook.js /var/www/html/hook.js

RUN rm /var/www/html/index.html
#RUN apachectl start
