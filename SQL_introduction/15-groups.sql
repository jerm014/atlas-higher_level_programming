 -- "The proper use of comments is to compensate for our failure to express
-- ourself in code." --Robert C. Martin (Author of Clean Code)
--
-- Make sure you put in a comment so everyone knows that this simple command
-- computes the score average of all records in the table
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY number, score
ORDER BY number DESC;
