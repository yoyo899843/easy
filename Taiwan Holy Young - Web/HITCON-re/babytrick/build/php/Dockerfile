# Use a base PHP image with Apache and PHP 5.6
FROM pr0ph3t/lamp

# Set working directory in the container
WORKDIR /var/www/html

# Copy the PHP application files to the container
COPY src/ /var/www/html/
# The base image ships a stale default Apache placeholder page here, which
# outranks index.php in DirectoryIndex order and shadows the challenge.
RUN rm -f /var/www/html/index.html

# Bridge PHP 5.x mysql_* calls (this challenge's code) to this image's PHP 7.0
# mysqli (see mysql_compat.php for why). The mysqli extension itself isn't
# installed on this image, and this image's Ubuntu 16.04 apt repos are EOL
# (no reachable Release file, even via old-releases.ubuntu.com), so the
# .deb is vendored here and installed directly instead of via apt.
COPY php7.0-mysql_7.0.8-3ubuntu3_amd64.deb /tmp/php7.0-mysql.deb
RUN dpkg -i --force-depends /tmp/php7.0-mysql.deb && rm -f /tmp/php7.0-mysql.deb
COPY mysql_compat.php /var/www/mysql_compat.php
RUN echo "auto_prepend_file=/var/www/mysql_compat.php" > /etc/php/7.0/apache2/conf.d/99-mysql-compat.ini

# Update the Apache configuration to enable .htaccess files
RUN a2enmod rewrite
#Create run.sh
ADD init.sql /var/www/

ADD run.sh /
RUN chmod +x /run.sh
# Expose port 80 for Apache
EXPOSE 80

# Start Apache server when the container runs
CMD ["bash", "-x", "/run.sh"]