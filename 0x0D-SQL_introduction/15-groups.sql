-- Create a query that counts the number of students who received each score in the second_table.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
