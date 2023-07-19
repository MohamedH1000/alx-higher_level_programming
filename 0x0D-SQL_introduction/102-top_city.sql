--  the top of 3 cities to be displayed
-- number of row selected to be limited
SELECT city, avg(value) as avg_temp 
FROM temperatures
WHERE (month = 7 OR month = 8)
GROUP BY city  
ORDER BY 2 DESC LIMIT 3;
