FROM php:8.0-apache
ARG CHAL_DOMAIN
RUN mkdir /secret && chown -R www-data /secret && chmod -R g+r /secret
RUN mkdir /etc/myssl
COPY ssl/fullchain.pem /etc/myssl/fullchain.pem 
COPY ssl/privkey.pem /etc/myssl/privkey.pem 
COPY src/index-secret.php /secret/index.php
COPY src/index.php /var/www/html/index.php
COPY sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN sed -i 's/<ReplaceWithSSLCertFile>/\/etc\/myssl\/fullchain.pem/g' /etc/apache2/sites-available/default-ssl.conf
RUN sed -i 's/<ReplaceWithSSLCertKeyFile>/\/etc\/myssl\/privkey.pem/g' /etc/apache2/sites-available/default-ssl.conf
RUN sed -i 's/<ReplaceWithServerIP>/18.163.8.31/g' /etc/apache2/sites-available/default-ssl.conf
#RUN sudo certbot certonly --webroot -w /var/www/html -d ${CHAL_DOMAIN} --agree-tos -m genden80@gmail.com --non-interactive
RUN a2enmod ssl && service apache2 restart && a2enmod rewrite && a2ensite default-ssl && service apache2 restart
EXPOSE 30200
EXPOSE 30201