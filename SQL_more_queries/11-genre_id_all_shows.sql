-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id`;
