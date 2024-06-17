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
-- creates user_0d_1 and grants priviledges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
