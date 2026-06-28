# Use a base PHP image with Apache and PHP 5.6
FROM pr0ph3t/lamp

# Set working directory in the container
WORKDIR /var/www/html

# Copy the PHP application files to the container
COPY src/ /var/www/html/

# Update the Apache configuration to enable .htaccess files
RUN a2enmod rewrite
#Create run.sh
ADD init.sql /var/www/

ADD run.sh /
RUN chmod +x /run.sh
# Expose port 80 for Apache
EXPOSE 80

# Start Apache server when the container runs
CMD ["bash -x /run.sh"]