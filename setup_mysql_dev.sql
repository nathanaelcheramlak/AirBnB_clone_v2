-- Creating hbnb_dev_db database.
-- Privileges for new user (hbnb_dev).
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user that will connect from the local host.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for the user.
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Selects 'hbnb_dev_db' as the active database.
USE hbnb_dev_db;
-- Grants privileges for the user.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flushes Privileges.
FLUSH PRIVILEGES;
