/etc/init.d/apache2 start &
socat TCP-LISTEN:2111,reuseaddr,fork EXEC:/bin/flag &