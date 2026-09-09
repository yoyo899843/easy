CREATE TABLE user (
  ID INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  account TEXT NOT NULL,
  password TEXT NOT NULL
);
INSERT INTO user (ID, name, account, password) VALUES (1, 'John', 'J_account', 'J_password');
INSERT INTO user (ID, name, account, password) VALUES (2, 'Mary', 'M_account', 'M_password');
INSERT INTO user (ID, name, account, password) VALUES (3, 'Eve', 'E_account', 'E_password');
INSERT INTO user (ID, name, account, password) VALUES (4, 'Fizz', 'F_account', 'F_password');
INSERT INTO user (ID, name, account, password) VALUES (50, 'Crazy', 'C_account', 'ACTF{YURXMTYS4C1MiSwjPBZc}');
