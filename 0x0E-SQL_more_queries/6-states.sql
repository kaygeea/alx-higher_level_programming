-- Create the database - "hbtn_0d_usa", and the table - "states" in the hbtn_0d_usa DB.
-- DESCRIPTION:
--	a. column 1 = "id" of type INT, a PK with unique and not null constraints, as well as auto generated.
--	b. column 2 = "name" of type VARCHAR with a max of 256 chars and a not null constrain.
--
-- SPECS:
--	a. If the hbtn_0d_usa DB already exists, the script should not fail.
--	b. If the states table already exists, the script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
