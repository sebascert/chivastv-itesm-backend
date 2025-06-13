DROP PROCEDURE IF EXISTS registrar_usuario;
DELIMITER //
CREATE PROCEDURE registrar_usuario(
    IN email VARCHAR(255),
    IN password_hash VARCHAR(255),
    IN nombre VARCHAR(100),
    IN apellido VARCHAR(100)
)
BEGIN
    INSERT INTO usuario (email, password_hash, nombre, apellido)
    VALUES (email, password_hash, nombre, apellido);
END;
//
DELIMITER ;
