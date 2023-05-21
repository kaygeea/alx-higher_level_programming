-- List records with scores => 10 from "second_table" table of htbn_0c_0 DB.
-- Result-set should display only score and name columns.
-- Result-set should be ordered by highest score first.
SELECT score, name FROM second_table WHERE score>9 ORDER BY score DESC;
