-- all shows from database to be listed
SELECT tv_shows.title,SUM(tv_show_ratings.rate) rating 
    FROM tv_shows
    INNER JOIN tv_show_ratings on tv_shows.id = tv_show_ratings.show_id 
    GROUP BY tv_shows.title 
    ORDER BY 2 DESC;
