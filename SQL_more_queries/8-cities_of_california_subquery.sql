-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
-- NOT ALLOWING A JOIN HERE IS CRIMINAL.
SELECT `id`, `name` FROM `cities` 
WHERE `state_id` = (SELECT `id` FROM `state`s WHERE `name` = 'California') 
ORDER BY `id`;
