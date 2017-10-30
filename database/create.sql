CREATE TABLE users (
  name VARCHAR(20) PRIMARY KEY,
  ip VARCHAR(12),
  pubKey CHAR(800),
  creacion DATETIME default current_timestamp
);
