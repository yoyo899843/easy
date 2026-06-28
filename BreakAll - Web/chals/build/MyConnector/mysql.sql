use mysql;
INSERT INTO user(host,user,password) VALUES('%','kaibro',password('superbig'));
GRANT SELECT ON *.* TO 'kaibro'@localhost IDENTIFIED BY 'superbig' WITH GRANT OPTION;
FLUSH PRIVILEGES;
