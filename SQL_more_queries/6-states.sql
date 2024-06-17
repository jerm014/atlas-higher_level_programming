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
-- creates database hbtn_0d_usa 
-- creates table states NEVER USE INTS FOR PK EVEN ON STATES
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT UNIQUE NOT NULL AUTO_INCREMENT, 
    `name` VARCHAR(256) NOT NULL, PRIMARY KEY(`id`)
    );
