-- all the number of the score to be counted and listed with score
--  by cluasela to be grouped
SELECT score, COUNT(score) as number 
FROM second_table
GROUP by score
ORDER by 1 DESC;
