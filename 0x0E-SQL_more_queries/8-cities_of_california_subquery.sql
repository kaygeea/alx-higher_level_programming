-- List all the cities of California that can be found in the database hbtn_0d_usa.
-- SPECS:
--	a. The "states" table in the hbtn_0d_usa DB has 2 columns, with just 1 record:
--		- "name"  = California
--		- "id" = may contain different values.
--	b. The result-set must be sorted in ascending order by the "id" column of the cities table.
--	c. JOIN keyword is prohibited.
SELECT id, name FROM cities
WHERE
id IN (SELECT id FROM states) = 1
ORDER BY id ASC;
