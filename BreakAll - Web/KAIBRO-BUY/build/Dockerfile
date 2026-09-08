FROM php:7.4-apache

COPY index.php /var/www/html/index.php
COPY login.php /var/www/html/login.php
COPY logout.php /var/www/html/logout.php
COPY dialog-polyfill.js /var/www/html/dialog-polyfill.js
COPY style.css /var/www/html/style.css
COPY vue.min.js /var/www/html/vue.min.js

RUN rm -f /var/www/html/index.html
