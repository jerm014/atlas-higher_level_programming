-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
-- THESE TABLES SHOULD BE ALIASED.
SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities` 
LEFT JOIN `states` ON `states`.`id` = `cities`.`state_id`
ORDER BY `cities`.`id`;
