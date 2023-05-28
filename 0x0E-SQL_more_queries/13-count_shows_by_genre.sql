-- List all genres from the hbtn_0d_tvshows DB and display the number of shows linked to each.
-- SPECS:
--	a. Each record should display: <TV Show genre> - <Number of shows linked to this genre>.
--	b. First column must be called "genre".
--	c. Second column must be called "number_of_shows".
--	d. Only genres with linked shows should be displayed.
--	e. The result-set must be sorted in descending order by the number of shows linked.
--	f. Only 1 SELECT statement is allowed in the query.
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
  FROM tv_genres
       LEFT JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
 GROUP BY genre
 ORDER BY number_of_shows DESC;
