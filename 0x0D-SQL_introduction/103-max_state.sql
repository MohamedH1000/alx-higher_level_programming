-- each state max temp to be displayed
-- a function that is max()
SELECT state, MAX(VALUE) as max_temp
FROM temperatures 
GROUP BY STATE 
ORDER BY 1;
