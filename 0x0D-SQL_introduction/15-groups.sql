-- script to display score and the number of times it occurs
SELECT score, COUNT(score) AS number 
FROM second_table 
GROUP BY score
ORDER BY score DESC;
