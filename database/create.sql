CREATE TABLE users (
  name VARCHAR(20) PRIMARY KEY NOT NULL,
  ip VARCHAR(12) NOT NULL,
  port INT NOT NULL,
  pubKey CHAR(800) NOT NULL,
  creacion DATETIME default current_timestamp NOT NULL
);
