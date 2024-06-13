 -- "The proper use of comments is to compensate for our failure to express
-- ourself in code." --Robert C. Martin (Author of Clean Code)
--
-- Make sure you put in a comment so everyone knows that this simple command
-- show some records but not if the name is null (the name and id column should
-- have been NOT NULL and the id column should have been set as a primary key.
-- but I didn't write this project. It would have been a lot more fun if I had.)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
