-- Creates the database hbnb_test_db with given paramenters.
-- Creates database.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a user that will connect from the local host.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Sets password for the user.
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grants Permissions for the user.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flushes Privileges.
FLUSH privileges;
