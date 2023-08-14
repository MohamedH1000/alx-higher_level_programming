--  all genres to be listed
SELECT tv_genres.name, SUM(tv_show_ratings.rate) rating
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings on tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY 2 DESC;
