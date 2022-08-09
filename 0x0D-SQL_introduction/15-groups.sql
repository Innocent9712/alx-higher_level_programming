-- script to display score and the number of times it occurs
SELECT score, COUNT(score) as number from second_table GROUP BY score;
