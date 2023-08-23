-- Creates a mysql server with:
  -- A database hbnb_dev_db
  -- User hbnb_dev with password hbnb_dev_pwd on localhost
  -- Grant all privileges for hbnb_dev on the database hbnb_dev_db
  -- Grant SELECT privilege for hbnb_dev on the database performance_schema

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- GrantSELECT privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
