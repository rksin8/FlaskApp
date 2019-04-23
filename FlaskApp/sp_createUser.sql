use FlaskBlogApp;


DROP PROCEDURE IF EXISTS sp_createUser;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(85)
)
BEGIN
    IF ( select exists (select 1 from blog_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into blog_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;


SHOW PROCEDURE STATUS WHERE db = 'FlaskBlogApp';
