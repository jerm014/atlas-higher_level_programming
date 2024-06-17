-- Commenting code is almost always considered bad practice.
--
-- A common excuse to comment on code is to improve poorly written code. This
-- is a mistake most beginners or even advanced developers make.
--
-- Instead of commenting on code, rewrite it!
--
-- The code should always be clear enough to express itself.
--
SELECT 
    `tv_genres`.`name` AS 'genre', 
    COUNT(`tv_show_genres`.`genre_id`) AS 'number_of_shows'
FROM `tv_genres`
RIGHT JOIN `tv_show_genres` ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
GROUP BY `genre`
ORDER BY `number_of_shows` DESC;
