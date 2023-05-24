-- Create the table - "force_name".
-- DESCRIPTION:
--	a. column 1 = "id" of type INT.
--	b. column 2 = "name" of type VARCHAR(256) and cannot be NULL.
--	c. IF force_name already exists, the script should not fail.
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
