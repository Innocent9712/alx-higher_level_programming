-- script to list all records with a name ordered by count in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
