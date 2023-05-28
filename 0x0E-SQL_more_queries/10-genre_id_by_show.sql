-- List all shows in the hbtn_0d_tvshows DB that have at least one genre linked.
-- SPECS:
--	a. Each record should display: tv_shows.title - tv_show_genres.genre_id.
--	b. The result set must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
--	c. Only 1 SELECT statement is allowed in the query.
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
       INNER JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
