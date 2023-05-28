-- List all Comedy shows in the database hbtn_0d_tvshows
-- SPECS:
--      a. The tv_genres table contains only one record where name = Comedy.
--      b. Each record should display: tv_shows.title.
--      c. The result set must be sorted in ascending order by the show title.
--      d. Only 1 SELECT statement is allowed in the query.
SELECT tv_shows.title
  FROM tv_shows
       INNER JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       INNER JOIN tv_genres
       ON tv_show_genres.genre_id = tv_genres.id
       WHERE tv_genres.name = "Comedy"
 ORDER BY tv_shows.title;
