CREATE SCHEMA `TestAB`;
SHOW schemas;
CREATE TABLE `TestAB`.`Product` (maker VARCHAR(50) NOT NULL, model VARCHAR (50) PRIMARY KEY auto_increment, type VARCHAR (50) NOT NULL);
SHOW TABLES;
CREATE TABLE `testab`.`pc`(
`codeX` INT NOT NULL PRIMARY KEY,
`model` VARCHAR(50) NOT NULL,
`speed` SMALLINT NOT NULL,
`RAM` SMALLINT NOT NULL,
`HD` REAL(12,2) NOT NULL,
`CD` VARCHAR (25) NOT NULL,
`money` SMALLINT NOT NULL);
CREATE TABLE `testab`.`laptop`(
`code` INT NOT NULL PRIMARY KEY auto_increment,
`model` VARCHAR(50) NOT NULL,
`speed` SMALLINT NOT NULL,
`RAM` SMALLINT NOT NULL,
`HD` REAL (12,2) NOT NULL,
`price` SMALLINT NOT NULL,
`screen` TINYINT NOT NULL);
CREATE TABLE `testab`.`printer`(
`code` INT NOT NULL PRIMARY KEY auto_increment,
`model` VARCHAR(50) NOT NULL,
`color` CHAR(1) NOT NULL,
`type` VARCHAR(10) NOT NULL,
`price` SMALLINT NOT NULL);
SHOW TABLES;
INSERT INTO product (maker,model,type) VALUES ('test','testt','tes');
SELECT * FROM product;
ALTER TABLE pc ADD foreign key (model) REFERENCES product(model);
ALTER TABLE printer ADD foreign key (model) references product(model);
ALTER TABLE laptop ADD foreign key (model) references product(model);
SHOW TABLES;