-- List all genres of the show "Dexter".
-- SPECS:
--	a. The tv_shows table contains only one record where title = Dexter.
--	b. Each record should display: tv_genres.name.
--	c. Results must be sorted in ascending order by the genre name.
--	d. Only 1 SELECT statement is allowed in the query.
SELECT tv_genres.name
  FROM tv_genres
       INNER JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
       INNER JOIN tv_shows
       ON tv_show_genres.show_id = tv_shows.id
       WHERE tv_shows.title = "Dexter"
 ORDER BY tv_genres.name;
