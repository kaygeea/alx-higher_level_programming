-- List all cities contained in the database - "hbtn_0d_usa".
-- SPECS:
--	a. Each record should display according to this column arrangement: cities.id - cities.name - states.name.
--	b. The results must be sorted in ascending order by cities.id.
--	c. Only 1 select statement if allowed in the query.
    SELECT cities.id, cities.name, states.name
      FROM cities
INNER JOIN states
        ON cities.id = states.id
  ORDER BY cities.id;
