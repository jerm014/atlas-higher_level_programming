-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
-- Make sure you put in a comment so everyone knows that this simple command
-- creates a table and defaults the id with unique
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE, 
    `name` VARCHAR(256)
    );
