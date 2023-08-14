-- average temp to be displayed
-- by avg temp to be ordered
SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY 2 DESC;
