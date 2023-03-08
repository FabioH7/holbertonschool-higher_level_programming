-- list number of records with same score and their count
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
