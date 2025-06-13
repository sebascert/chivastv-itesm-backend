DROP PROCEDURE IF EXISTS login_usuario;
DELIMITER //
CREATE PROCEDURE login_usuario(
    IN email VARCHAR(255),
    IN password_hash VARCHAR(255)
)
BEGIN
    SELECT ID, email FROM usuario
    WHERE email = email AND password_hash = password_hash;
END;
//
DELIMITER ;
