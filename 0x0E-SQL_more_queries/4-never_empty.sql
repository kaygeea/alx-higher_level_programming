-- Create the table - "id_not_null".
-- DESCRIPTION:
--	a. column 1 = "id" of type INT and assigned a defualt value of 1.
--	b. column 2 = "name" of type VARCHAR(256).
-- SPECS:
--	a. If id_not_null already exists, your script should not fail.
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
