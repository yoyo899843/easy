FROM php:5.6-apache

# Debian stretch is EOL; point apt at the archive mirror and skip
# signature/expiry checks (the stretch release keys are long expired).
RUN printf 'deb [trusted=yes] http://archive.debian.org/debian stretch main\ndeb [trusted=yes] http://archive.debian.org/debian-security stretch/updates main\n' > /etc/apt/sources.list \
    && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

# index.php uses the classic mysql_* API (removed in PHP 7), and connects to
# a MySQL server on localhost - so this image needs PHP's legacy mysql
# extension plus a real local MySQL/MariaDB server, matching the original
# (now-dead) dockerfiles/centos-lamp all-in-one setup.
RUN apt-get update && apt-get install -y mariadb-server \
    && docker-php-ext-install mysql

# PHP's mysql extension defaults to a socket path that doesn't match where
# this Debian MariaDB actually puts its socket, so mysql_connect('localhost')
# fails with "No such file or directory".
RUN echo "mysql.default_socket = /run/mysqld/mysqld.sock" >> /usr/local/etc/php/conf.d/mysql-socket.ini

COPY index.php /var/www/html/index.php
COPY user.sql /user.sql
COPY mysql.sql /mysql.sql
COPY run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 80
CMD ["/run.sh"]
