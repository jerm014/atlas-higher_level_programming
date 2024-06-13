-- "The proper use of comments is to compensate for our failure to express
-- ourself in code." --Robert C. Martin (Author of Clean Code)
--
-- Make sure you put in a comment so everyone knows that this simple command
-- creates a table in a database specified on the command line
USE ?;
CREATE TABLE IF NOT EXISTS first_table (id int, name VARCHAR(256));
