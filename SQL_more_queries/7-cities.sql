-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`state_id`) REFERENCES `states`(`id`)
    );
