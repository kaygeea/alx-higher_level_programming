-- Create the database - "hbtn_0d_usa", and the table - "cities" in the hbtn_0d_usa DB.
-- DESCRIPTION (of cities table):
--	a. column 1 = "id" of type INT, a PK with unique and not null constraints, as well as auto generated.
--	b. column 2 = "state_id" of type INT, a FK that references the "id" column of the states table and cannot be null.
--	c. column 3 = "name" of type VARCHAR with a max of 256 chars and a not null constrain.
--
-- SPECS:
--	a. If the hbtn_0d_usa DB already exists, the script should not fail.
--	b. If the cities table already exists, the script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT cities_fk
	FOREIGN KEY (state_id)
	REFERENCES states(id)
);
