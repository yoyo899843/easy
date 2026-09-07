FROM php:7.4-apache

RUN apt-get update \
    && apt-get install -y --no-install-recommends unzip \
    && rm -rf /var/lib/apt/lists/*

COPY custom-apache.conf /etc/apache2/conf-available/custom-apache.conf
RUN ln -s /etc/apache2/conf-available/custom-apache.conf /etc/apache2/conf-enabled/custom-apache.conf

ADD src /var/www/html

# The leak is the .git directory itself, not a downloadable archive:
# unpack it at build time and drop the zip so it is never served.
RUN cd /var/www/html \
    && unzip -q git.zip \
    && rm -f git.zip \
    && chown -R www-data:www-data /var/www/html

EXPOSE 80
