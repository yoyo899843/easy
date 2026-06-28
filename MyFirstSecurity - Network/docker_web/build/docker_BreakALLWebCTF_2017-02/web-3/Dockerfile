FROM ubuntu:14.04

RUN apt-get update && apt-get install -y apache2 libapache2-mod-php5 zip

COPY www/ /var/www/html/
COPY flag //

EXPOSE 80

ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
