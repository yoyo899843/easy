FROM php:7.2-apache
COPY src/ /var/www/html/
WORKDIR /app
COPY ./install ./
COPY flagfile /app/
RUN dpkg -i Neo-cowsay_2.0.4_linux_amd64.deb
RUN cowsay