-- Create the database - "hbtn_0d_2" and the user - "user_0d_2".
-- SPECS:
--	a. user_0d_2 should have only SELECT privilege in the DB hbtn_0d_2.
--	b. The user_0d_2 password should be set to "user_0d_2_pwd".
--	c. If the DB hbtn_0d_2 already exists, your script should not fail.
--	d. If the user user_0d_2 already exists, your script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_02_2.* TO 'user_0d_2'@'localhost';
