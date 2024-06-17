-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
SELECT `title`
FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
LEFT JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
WHERE `tv_genres`.`name` = 'Comedy'
GROUP BY `title`
ORDER BY `title`;
