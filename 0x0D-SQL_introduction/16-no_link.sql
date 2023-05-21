-- List records from second_table
-- SPECS:
--	a. Do not list any row without a name value.
--	b. The result-set should display only the score and name columns.
--	c. The result-set should be sorted in descending order of the scores.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
