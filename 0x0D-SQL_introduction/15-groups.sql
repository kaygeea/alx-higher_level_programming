-- List the number of records with the same score in second_table
-- SPECS:
--	a. The result-set should display the score.
--	b. The result-set should display the number of records for each score under the label "number".
--	c. The result-set should be sorted, in descending order, by the number of records.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
