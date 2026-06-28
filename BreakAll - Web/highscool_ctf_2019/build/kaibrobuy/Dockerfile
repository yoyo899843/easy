FROM nimmis/apache-php7
#RUN apt-get update

COPY index.php /var/www/html/index.php
COPY login.php /var/www/html/login.php
COPY logout.php /var/www/html/logout.php
COPY dialog-polyfill.js /var/www/html/dialog-polyfill.js
COPY style.css /var/www/html/style.css
COPY vue.min.js /var/www/html/vue.min.js

RUN rm /var/www/html/index.html
#RUN apachectl start
