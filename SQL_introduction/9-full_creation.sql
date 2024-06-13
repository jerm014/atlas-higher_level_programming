-- "The proper use of comments is to compensate for our failure to express
-- ourself in code." --Robert C. Martin (Author of Clean Code)
--
-- Make sure you put in a comment so everyone knows that this simple command
-- shows the count of records in a table in a database specified on the command line
USE ?;
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (1,'John',10),(2,'Alex',3),(3,'Bob',14),(4,'George',8);
