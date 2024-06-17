-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
SELECT `name` FROM tv_genres
LEFT JOIN `tv_show_genres` ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
LEFT JOIN `tv_shows` ON `tv_show_genres`.`show_id` = `tv_shows`.`id`
WHERE `tv_shows`.`title` = 'Dexter'
GROUP BY `name`
ORDER BY `name`;
