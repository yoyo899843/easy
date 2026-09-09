FROM php:8.3-cli-alpine

WORKDIR /var/www/html
COPY www/ /var/www/html/
COPY init.sql /tmp/init.sql

# Seed a local SQLite DB at build time (pdo_sqlite is bundled in the official image),
# so the challenge needs no separate database server.
RUN php -r '$d = new PDO("sqlite:/var/www/html/app.db"); foreach (array_filter(array_map("trim", explode(";", file_get_contents("/tmp/init.sql")))) as $s) { $d->exec($s); }' \
    && rm /tmp/init.sql \
    && chmod 664 /var/www/html/app.db

EXPOSE 80
CMD ["php", "-S", "0.0.0.0:80", "-t", "/var/www/html"]
