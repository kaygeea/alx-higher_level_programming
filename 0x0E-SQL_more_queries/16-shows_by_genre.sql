-- List all shows, and all genres linked to each show, from the database hbtn_0d_tvshows.
-- SPECS:
--	a. If a show doesn’t have a genre, display "NULL" in the genre column.
--	b. Each record should display: tv_shows.title - tv_genres.name
--	c. The result set must be sorted in ascending order by the show title and genre name.
--	d. Only 1 SELECT statement is allowed in the query.
SELECT tv_shows.title, tv_genres.name
  FROM tv_shows
       LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       LEFT JOIN tv_genres
       ON tv_show_genres.genre_id = tv_genres.id
 ORDER BY tv_shows.title, tv_genres.name;
