FROM nimmis/apache-php7
#RUN apt-get update

RUN apt update
RUN apt install dnsutils -y

COPY index.php /var/www/html/index.php
COPY bootstrap.css /var/www/html/bootstrap.css
COPY flag /flag

RUN rm /var/www/html/index.html
#RUN apachectl start
