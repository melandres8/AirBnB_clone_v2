-- Creates the database hbnb_test_db in the MySQL server
-- Creates a new user 'hbnb_test' (in localhost) with password of 'hbnb_test_pwd'
-- Grants all privileges on the database hbnb_test_db to hbnb_test
-- Grants SELECT privilege on the database performance_schema to hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
