-- List records from "second_table" table of htbn_0c_0 DB
-- Result-set should display only score and name columns.
-- Result-set should be ordered by highest score first.
SELECT score, name FROM second_table ORDER BY score DESC;
