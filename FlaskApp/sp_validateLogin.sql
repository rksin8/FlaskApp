use FlaskBlogApp;

/* DROP PROCEDURE IF EXISTS sp_validateLogin; */

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(IN p_username VARCHAR(45) )
BEGIN
    select * from blog_user where user_username = p_username;
END$$

DELIMITER ;


/* SHOW PROCEDURE STATUS WHERE db = 'FlaskBlogApp'; */

