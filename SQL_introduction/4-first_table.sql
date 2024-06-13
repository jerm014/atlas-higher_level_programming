-- Make sure you put in a comment so everyone knows that this simple command
-- creates a table in a database specified on the command line
USE ?;
CREATE TABLE IF NOT EXISTS first_table (id int, name VARCHAR(256));
