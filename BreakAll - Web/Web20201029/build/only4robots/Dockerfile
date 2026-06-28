FROM php:7.3-apache
MAINTAINER RB363
RUN apt update

WORKDIR /var/www/html

COPY index.html .
COPY robots_bce7cbb93aae990d0ae6642b96eb2e8753639b8.php .
COPY .htaccess .
COPY flag_2cf61812c352ec4fd0dae8f52874701d.txt .

RUN service apache2 start
RUN echo "<Directory /var/www/html>" >> /etc/apache2/sites-available/000-default.conf
RUN echo "Options Indexes FollowSymLinks" >> /etc/apache2/sites-available/000-default.conf
RUN echo "AllowOverride All" >> /etc/apache2/sites-available/000-default.conf
RUN echo "Require all granted" >> /etc/apache2/sites-available/000-default.conf
RUN echo "</Directory>" >> /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite
RUN service apache2 restart
