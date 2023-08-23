-- Prepare a MYSQL server
  -- A database hbnb_test_db
  -- A new user hbnb_test on localhost with password hbnb_test_pwd
  -- Grant all privileges on database hbnb_test_db to hbnb_test
  -- Grant SELECT privilege on database performance_schema to hbnb_test

-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
