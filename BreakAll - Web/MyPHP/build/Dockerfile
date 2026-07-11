FROM dockerfiles/centos-lamp 
#RUN apt-get update

COPY www/ /var/www/html/

RUN rm /var/www/html/phpinfo.php
#RUN apachectl start
EXPOSE 80
