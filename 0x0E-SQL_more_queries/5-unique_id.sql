-- Create the table - "unique_id".
-- DESCRIPTION:
--	a. column 1 = "id" of type INT, with a default of 1 and a unique constraint.
--	b. column 2 = "name" of type VARCHAR with a max of 256 chars.
-- SPECS:
--	a. If unique_id already exists, the script should not fail.
CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
