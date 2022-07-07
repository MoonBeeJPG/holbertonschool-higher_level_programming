-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genre.name AS genre, COUNT(*) AS number_of_shows FROM tv_shows genre
INNER JOIN tv_show_genres tvg ON genre.id = tvg.genre_id
GROUP BY genre.name
ORDER BY number_of_shows DESC;
